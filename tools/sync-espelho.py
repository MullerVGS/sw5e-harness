#!/usr/bin/env python3
"""Sincroniza o espelho de regras de SW5e a partir da API pública da comunidade.

Baixa as nove coleções, escreve uma fatia por entidade sob `sw5e/<colecao>/` e
gera o `INDEX.md` de cada coleção. Relata o que entrou, saiu ou mudou desde o
sync anterior.

Uso:
    python3 tools/sync-espelho.py [--api URL] [--destino DIR] [--dry-run]

Python 3 stdlib puro, sem dependência externa. Rodar de novo é seguro: a saída
é canônica, então uma segunda execução sem mudança na API não gera diff.
"""

import argparse
import json
import re
import sys
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path

API = "https://sw5eapi.azurewebsites.net"
TIMEOUT = 180
TENTATIVAS = 3

# Campos `*Json`/`*Enum` cuja contraparte parseada não existe e que, por isso,
# carregam informação própria: são convertidos e renomeados em vez de removidos.
CONVERTER = {
    "levelChangeHeadersJson": "levelChangeHeaders",
    "leveledTableHeadersJson": "leveledTableHeaders",
}

# Plumbing do Azure Table Storage, sem conteúdo de jogo. `partitionKey` é
# idêntico a `contentType` em todas as entidades; `eTag` deriva do `timestamp`.
DESCARTAR = ("eTag", "timestamp", "partitionKey")


def fatiar(colecao, pasta, resumo):
    return {"colecao": colecao, "pasta": pasta, "resumo": resumo}


# A API usa estas strings como "não se aplica" — um kit vem com
# `weaponClassification: "Unknown"`. Elas não entram no resumo do índice.
VAZIOS = {"", "unknown", "none", "n/a", "-"}


def val(entidade, *chaves):
    """Primeiro valor preenchido entre as chaves, ignorando os placeholders."""
    for chave in chaves:
        bruto = entidade.get(chave)
        if bruto is None:
            continue
        if isinstance(bruto, str):
            if bruto.strip().lower() in VAZIOS:
                continue
            return bruto.strip()
        return bruto
    return None


def _incrementos(ent):
    variantes = ent.get("abilitiesIncreased") or []
    if not variantes or not isinstance(variantes[0], list):
        return ""
    partes = []
    for item in variantes[0]:
        nomes = ", ".join(item.get("abilities") or [])
        if nomes:
            partes.append(f"{nomes} +{item.get('amount')}")
    return "; ".join(partes)


def resumo_especie(ent):
    partes = [val(ent, "size"), _incrementos(ent), val(ent, "homeworld")]
    if not any(partes):
        variantes = ent.get("halfHumanTableEntries") or {}
        if variantes:
            return f"híbrido · traço varia entre {len(variantes)} espécies"
    return " · ".join(p for p in partes if p)


def resumo_classe(ent):
    caster = val(ent, "casterType")
    if caster:
        ratio = ent.get("casterRatio") or 0
        caster = f"{caster} {ratio:g}".rstrip()
    salva = ", ".join(ent.get("savingThrows") or [])
    return " · ".join(
        p
        for p in (
            f"d{ent['hitDiceDieType']}" if ent.get("hitDiceDieType") else None,
            val(ent, "primaryAbility"),
            caster,
            f"salvaguardas {salva}" if salva else None,
        )
        if p
    )


def resumo_arquetipo(ent):
    return val(ent, "className") or ""


def resumo_background(ent):
    return val(ent, "skillProficiencies") or ""


def resumo_poder(ent):
    nivel = ent.get("level")
    alinhamento = val(ent, "forceAlignment")
    return " · ".join(
        p
        for p in (
            "at-will" if nivel == 0 else f"nível {nivel}",
            val(ent, "powerType"),
            alinhamento,
            val(ent, "castingPeriod"),
            val(ent, "range"),
            "concentração" if ent.get("concentration") else None,
        )
        if p
    )


def resumo_equipamento(ent):
    dano = None
    if ent.get("damageNumberOfDice") and ent.get("damageDieType"):
        mod = ent.get("damageDieModifier") or 0
        dano = f"{ent['damageNumberOfDice']}d{ent['damageDieType']}"
        if mod:
            dano += f"{mod:+d}"
        tipo = val(ent, "damageType")
        if tipo:
            dano += f" {tipo}"
    custo = ent.get("cost")
    return " · ".join(
        p
        for p in (
            val(ent, "equipmentCategory"),
            val(ent, "armorClassification", "weaponClassification"),
            f"CA {ent['ac']}" if val(ent, "ac") else None,
            dano,
            f"{custo} cr" if custo else None,
        )
        if p
    )


def resumo_feat(ent):
    pre = val(ent, "prerequisite")
    return f"pré-req: {pre}" if pre else "sem pré-requisito"


def resumo_monstro(ent):
    tipos = ent.get("types") or []
    tipo = ", ".join(t for t in tipos if t) if isinstance(tipos, list) else str(tipos)
    cr = ent.get("challengeRating")
    return " · ".join(
        p
        for p in (
            f"CR {cr}" if cr is not None else None,
            " ".join(x for x in (val(ent, "size"), tipo) if x) or None,
            f"CA {ent['armorClass']}" if ent.get("armorClass") else None,
            f"{ent['hitPoints']} PV" if ent.get("hitPoints") else None,
        )
        if p
    )


def resumo_item(ent):
    pre = val(ent, "prerequisite")
    return " · ".join(
        p
        for p in (
            val(ent, "type"),
            val(ent, "subtype"),
            val(ent, "rarityText", "searchableRarity"),
            "sintonia" if ent.get("requiresAttunement") else None,
            f"pré-req: {pre}" if pre else None,
        )
        if p
    )


COLECOES = [
    fatiar("species", "especies", resumo_especie),
    fatiar("class", "classes", resumo_classe),
    fatiar("archetype", "arquetipos", resumo_arquetipo),
    fatiar("background", "backgrounds", resumo_background),
    fatiar("power", "poderes", resumo_poder),
    fatiar("equipment", "equipamentos", resumo_equipamento),
    fatiar("feat", "feats", resumo_feat),
    fatiar("monster", "monstros", resumo_monstro),
    fatiar("enhancedItem", "itens", resumo_item),
]


def baixar(api, colecao):
    url = f"{api}/api/{colecao}"
    ultimo = None
    for tentativa in range(1, TENTATIVAS + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "sw5e-harness/sync-espelho"})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (urllib.error.URLError, OSError, json.JSONDecodeError) as erro:
            ultimo = erro
            if tentativa < TENTATIVAS:
                print(f"    tentativa {tentativa} falhou ({erro}); repetindo", file=sys.stderr)
    raise SystemExit(f"erro: não consegui baixar {url}: {ultimo}")


def slug(texto):
    texto = unicodedata.normalize("NFKD", str(texto or ""))
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    texto = re.sub(r"[^a-zA-Z0-9]+", "-", texto).strip("-").lower()
    return texto or "sem-nome"


def nomear(entidades):
    """Um nome de arquivo por entidade, estável e independente da ordem da API.

    O nome sai do `name`. Onde dois nomes colidem — três casos hoje — o grupo
    inteiro ganha discriminador, para que a ordem da resposta da API não decida
    quem fica com o nome limpo.
    """
    grupos = {}
    for ent in entidades:
        grupos.setdefault(slug(ent.get("name")), []).append(ent)

    nomes = {}
    for base, grupo in grupos.items():
        if len(grupo) == 1:
            nomes[id(grupo[0])] = base
            continue
        chaves = [slug(e.get("rowKey")) for e in grupo]
        if len(set(chaves)) == len(grupo):
            candidatos = chaves
        else:
            candidatos = [f"{base}-{slug(e.get('contentSource'))}" for e in grupo]
        if len(set(candidatos)) != len(grupo):
            ordenado = sorted(grupo, key=lambda e: (str(e.get("rowKey")), str(e.get("contentSource"))))
            candidatos = [f"{base}-{ordenado.index(e) + 1}" for e in grupo]
        for ent, nome in zip(grupo, candidatos):
            nomes[id(ent)] = nome
    return nomes


def limpar(valor, avisos, trilha=""):
    """Remove duplicações provadas da entidade, recursivamente.

    Sai fora todo `*Json`/`*Enum` cuja contraparte parseada existe ao lado — são
    serializações e códigos numéricos do mesmo dado. Órfão desconhecido fica e
    é avisado: se a API ganhar campo novo, o sync reclama em vez de perdê-lo.
    """
    if isinstance(valor, list):
        return [limpar(v, avisos, trilha) for v in valor]
    if not isinstance(valor, dict):
        return valor

    saida = {}
    for chave, bruto in valor.items():
        if chave in DESCARTAR:
            continue
        if chave in CONVERTER:
            texto = (bruto or "").strip() if isinstance(bruto, str) else bruto
            if isinstance(texto, str) and texto:
                try:
                    bruto = json.loads(texto)
                except json.JSONDecodeError:
                    pass
            saida[CONVERTER[chave]] = limpar(bruto, avisos, trilha)
            continue
        if chave.endswith(("Json", "Enum")):
            raiz = chave[:-4]
            pares = [raiz, raiz + "s"] if not raiz.endswith("s") else [raiz, raiz[:-1]]
            if any(p in valor for p in pares):
                continue
            avisos.add(f"{trilha}{chave}")
        saida[chave] = limpar(bruto, avisos, f"{trilha}{chave}.")
    return saida


def _ordem(chave):
    return (0, int(chave), "") if str(chave).isdigit() else (1, 0, str(chave))


def canonizar(valor):
    """Reordena as chaves para que a saída não dependa da ordem da API.

    Chave numérica ordena por número — a tabela de níveis de uma classe sai
    1, 2, ..., 20, não 1, 10, 11.
    """
    if isinstance(valor, dict):
        return {c: canonizar(valor[c]) for c in sorted(valor, key=_ordem)}
    if isinstance(valor, list):
        return [canonizar(v) for v in valor]
    return valor


def serializar(entidade):
    return json.dumps(canonizar(entidade), indent=2, ensure_ascii=False) + "\n"


def montar_index(spec, entidades, nomes):
    linhas = [
        f"# {spec['pasta']} — {len(entidades)} entidades",
        "",
        "Índice do espelho: escolha por aqui e só então abra a fatia. O arquivo é o",
        "nome em slug (minúsculas, hífens); onde o nome não basta, ele vem entre",
        "backticks na linha.",
        "",
    ]
    ordenado = sorted(entidades, key=lambda e: (str(e.get("name") or ""), nomes[id(e)]))
    for ent in ordenado:
        nome = ent.get("name") or "(sem nome)"
        arquivo = nomes[id(ent)]
        rotulo = f"**{nome}**" if arquivo == slug(nome) else f"**{nome}** (`{arquivo}.json`)"
        try:
            resumo = (spec["resumo"](ent) or "").strip()
        except Exception as erro:  # um resumo quebrado não pode derrubar o sync
            resumo = ""
            print(f"    aviso: resumo de {nome!r} falhou: {erro}", file=sys.stderr)
        resumo = " ".join(resumo.split())
        linhas.append(f"- {rotulo} — {resumo}" if resumo else f"- {rotulo}")
    return "\n".join(linhas) + "\n"


def sincronizar(spec, destino, api, dry_run):
    print(f"  {spec['colecao']} → {spec['pasta']}/", end="", flush=True)
    entidades = baixar(api, spec["colecao"])
    if not isinstance(entidades, list):
        raise SystemExit(f"erro: /api/{spec['colecao']} não devolveu uma lista")

    avisos = set()
    nomes = nomear(entidades)
    novos = {f"{nomes[id(e)]}.json": serializar(limpar(e, avisos)) for e in entidades}
    novos["INDEX.md"] = montar_index(spec, entidades, nomes)

    pasta = destino / spec["pasta"]
    antigos = {}
    if pasta.is_dir():
        for arq in pasta.iterdir():
            if arq.is_file() and arq.suffix in (".json", ".md"):
                antigos[arq.name] = arq.read_text(encoding="utf-8")

    entrou = sorted(set(novos) - set(antigos))
    saiu = sorted(set(antigos) - set(novos))
    mudou = sorted(n for n in set(novos) & set(antigos) if novos[n] != antigos[n])

    if not dry_run:
        pasta.mkdir(parents=True, exist_ok=True)
        for nome in entrou + mudou:
            (pasta / nome).write_text(novos[nome], encoding="utf-8")
        for nome in saiu:
            (pasta / nome).unlink()

    print(f" {len(entidades)} entidades", end="")
    if avisos:
        print(f"\n    campo novo mantido por precaução: {', '.join(sorted(avisos))}", end="")
    return entrou, saiu, mudou, len(entidades)


def main():
    p = argparse.ArgumentParser(description="Sincroniza o espelho de regras de SW5e.")
    p.add_argument("--api", default=API, help=f"base da API (default: {API})")
    p.add_argument("--destino", default=None, help="pasta do espelho (default: sw5e/ na raiz do repo)")
    p.add_argument("--dry-run", action="store_true", help="não escreve nada; só relata")
    args = p.parse_args()

    destino = Path(args.destino) if args.destino else Path(__file__).resolve().parent.parent / "sw5e"
    print(f"Espelho: {destino}")
    if args.dry_run:
        print("(dry-run: nada será escrito)")

    total = {"entrou": 0, "saiu": 0, "mudou": 0, "entidades": 0}
    detalhe = []
    for spec in COLECOES:
        entrou, saiu, mudou, n = sincronizar(spec, destino, args.api, args.dry_run)
        marcas = []
        if entrou:
            marcas.append(f"+{len(entrou)}")
        if saiu:
            marcas.append(f"-{len(saiu)}")
        if mudou:
            marcas.append(f"~{len(mudou)}")
        print(f"  [{' '.join(marcas)}]" if marcas else "  [sem mudança]")
        total["entrou"] += len(entrou)
        total["saiu"] += len(saiu)
        total["mudou"] += len(mudou)
        total["entidades"] += n
        for rotulo, itens in (("+", entrou), ("-", saiu), ("~", mudou)):
            for nome in itens:
                detalhe.append(f"  {rotulo} {spec['pasta']}/{nome}")

    print(f"\n{total['entidades']} entidades em {len(COLECOES)} coleções.")
    if total["entrou"] or total["saiu"] or total["mudou"]:
        print(f"Mudou desde o sync anterior: +{total['entrou']} entrou, -{total['saiu']} saiu, ~{total['mudou']} alterado.")
        corte = 40
        for linha in detalhe[:corte]:
            print(linha)
        if len(detalhe) > corte:
            print(f"  ... e mais {len(detalhe) - corte} arquivos")
    else:
        print("Nada mudou desde o sync anterior.")


if __name__ == "__main__":
    main()
