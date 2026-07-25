---
name: nova-campanha
description: Abre uma Campanha nova — entrevista o Jogador e escreve campanhas/<slug>/ com Contexto e Crônica. Use quando ele disser que vai entrar numa mesa nova, que vai mestrar uma campanha, ou pedir para registrar uma mesa que já joga.
---

# nova-campanha

Abre uma mesa. O que sair daqui é o que toda ficha vai ler depois — e o que o Jogador não vai mais ter que recontar.

## Ler antes

`CONTEXT-MAP.md` da raiz, só para não colidir de slug. Campanha nova não tem contexto para ler: é você que vai criá-lo.

Se o slug já estiver lá, é a mesma mesa — pergunte antes de tocar em qualquer coisa.

## A entrevista

Uma pergunta por vez. Pare quando as respostas fecharem o Contexto — não colete o que não vai para o arquivo.

O que você não tem como inferir:

1. **Nome e papel** — como a mesa se chama, e se ele joga ou mestra nela.
2. **Era e tom** — quando se passa, e que tipo de história é (intriga, guerra, contrabando...). Uma linha cada.
3. **O grupo** — quantos são, que nível, e quem é cada um em uma linha. Se ele mestra, o grupo é dos jogadores.
4. **Método de atributos** — point-buy, rolagem (qual), array padrão. É por perguntar aqui que `criar-personagem` não pergunta depois.
5. **Fontes permitidas** — tudo o que estiver no Espelho, ou a mesa restringe.
6. **Divergência do cânon** — o que a mesa inventou ou contradiz. Pergunte explícito: é a única parte do cenário que vira arquivo.
7. **Casa-regras** — o que a mesa mudou de mecânica.

Não pergunte planetas, facções, cronologia nem quem é quem no cânon: você já sabe, e anotar o que já se sabe é manutenção sem retorno. Só interessa a **postura** das facções em relação ao grupo.

Se a mesa já roda há tempo, pergunte também o que aconteceu até agora. Isso vira a primeira entrada da Crônica, não o Contexto.

## Escrever

Slug: nome em minúsculas, sem acento, com hífen — "O Cerco de Mandalore" → `cerco-de-mandalore`.

Não crie pasta vazia. `personagens/`, `npcs/` e `inimigos/` nascem com a primeira ficha.

### `campanhas/<slug>/CONTEXT.md`

Cabe numa tela, ou não é Contexto. Seção sem conteúdo fica com `_nenhuma_` — a Promoção precisa de onde escrever depois.

```markdown
# <Nome da campanha>

<papel do Jogador> · <era> · <tom em meia linha>

## Mesa

- **Nível do grupo**: <n>
- **Atributos**: <método>
- **Fontes**: <o que vale>
- **Casa-regras**: <o que mudou, ou _nenhuma_>

## O grupo

- **<Personagem> (<quem joga>)** — <Species Class N>, uma linha de quem é

## Facções e figuras

- **<Nome>** — <postura em relação ao grupo>

## Divergência do cânon

- <o que a mesa inventou ou contradiz>

## Situação

<2 a 4 linhas: onde o grupo está, o que está pendente, de quem está devendo.>
```

### `campanhas/<slug>/CRONICA.md`

Uma entrada por sessão, a mais recente **por último** — quem lê, lê a cauda. Por isso cada entrada se explica sozinha: quem estava, onde, e o que ficou.

O arquivo nasce com o cabeçalho abaixo, que é o que fixa o formato para a `registrar-sessao`:

```markdown
# Crônica — <Nome da campanha>

Uma entrada por sessão, a mais recente por último. Formato:

`## S<NN> — <AAAA-MM-DD> · <lugar>`, **Presentes**, 3 a 8 linhas do que
aconteceu nomeando quem apareceu, e **Promovido** com o que subiu para o
`CONTEXT.md` — ou `nada`.
```

E uma entrada fica assim:

```markdown
## S07 — 2026-07-18 · Nar Shaddaa, níveis inferiores

**Presentes**: Vessa, Talon, Rix-9

O grupo entregou o manifesto roubado a Bek Vandar e descobriu tarde que ele
já tinha vendido a informação ao cartel. Vessa negociou a saída; Rix-9 ficou
para trás cobrindo, e voltou com o braço queimado. Talon subiu de nível na
volta para a nave.

**Promovido**: Hutt Cartel virou hostil; Bek Vandar entrou como figura.
```

Se a mesa já rodava antes do registro, a primeira entrada é `## S00 — <data de hoje> · retroativo`, com o que ele contou na entrevista.

`Promovido` é o que fecha o ciclo: lendo a entrada, dá para saber se o Contexto já absorveu aquilo. `nada` é resposta boa e frequente.

### `CONTEXT-MAP.md`

Registre a campanha na seção Campanhas, no formato que já está lá. Se ainda estiver com `_(nenhuma campanha ainda)_`, substitua a linha.

## Fechar

Mostre o `CONTEXT.md` inteiro no chat — ele é pequeno — e pergunte o que está errado. É o momento mais barato de consertar.

Commite (`campanha: <Nome>`) e diga qual é o próximo passo: `criar-personagem`.
