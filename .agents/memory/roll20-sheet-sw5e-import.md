---
name: roll20-sheet-sw5e-import
description: Como o sheet SW5e do Roll20 importa JSON — limpa tudo antes, não recalcula nada, e os campos que o export omite (atkattr_base no PC, os *_flag no NPC) precisam ir à mão
metadata:
  type: reference
---

O sheet **StarWars5E** do Roll20 (fonte: `github.com/Roll20/roll20-character-sheets/tree/master/StarWars5E`,
arquivo `StarWars5E_HTML.html`) tem botão **Import From Json / Export To Json** na
aba de opções, esquema `Sheet-3.1`: `{schema_version, exportedBy, name, attribs: [{name,current,max,id}],
sections: [{section_name, rows:[{campo: valor}]}]}`. Verificado no código em 2026-07-25:

- **O import limpa a ficha inteira antes de aplicar** (remove toda linha repetida e
  zera os atributos das listas `pc_attrs`/`npc_attrs`/`power_attrs`) e **renomeia o
  personagem** para o `name` do JSON. Não precisa desfazer nada à mão.
- **Nada é recalculado no import**: os listeners ignoram mudanças vindas de sheetworker.
  Todo derivado vai pronto no JSON — `*_bonus` de perícia e salvaguarda, `ac`,
  `passive_wisdom`, `atkbonus` e os três `rollbase*` de cada ataque. O formato do
  `rollbase` é o que o worker geraria (labels `[DEX]`/`[PROF]`; com `dtype=pick` é o
  template `atk` com dmg/crit separados). Ataque sem proficiência: `atkprofflag: "0"`.
- **Selects sem `value=` gravam o texto traduzido**: com o cliente em pt-BR, a fonte
  de um trait é `Racial`/`Classe`/`Talento`/`Antecedente`/`Outro` e o `prof_type` de
  armadura é `ARMADURA` (LANGUAGE e WEAPON não mudam). Selects com `value=` explícito
  (classe, `powerschool` force/tech, `powersave`) ficam em inglês.
- **Pegadinhas de campo**: `tech_power_points_expended` é exibido como *remaining*
  (ficha nova = total); expertise de perícia é `<skill>_type: 2` com prof
  `(@{pb}*@{<skill>_type})`; AC automática lê `itemmodifiers` do item equipado no
  formato `Item Type: Light Armor, AC: 11`; o atributo de ataque é `atkattr_base`
  (valor `power` usa a habilidade de conjuração) e ele *não sai no export* — o export
  lista `atkbase` por engano, então incluir `atkattr_base` à mão no JSON de import.
- O poder at-will que escala grava `power_damage_progression: "Cantrip Dice"`.
- **O lado NPC é outra ficha dentro da mesma**: `npc: "1"` a liga (`0` = PC, `2` =
  nave), e o nome vai em `npc_name`, não só no `name` do JSON. As seções são
  `repeating_npctrait` (só `name`/`desc`) e `repeating_npcaction`; o import gera
  os IDs de linha sozinho, então `id` não precisa ser mandado.
- **Perícia de NPC são três campos**: `npc_<skill>_base` guarda o bônus,
  `npc_<skill>` repete o valor para exibição e `npc_<skill>_flag` diz como
  renderizar (`2` no último listado, `1` nos demais, `4`/`3` se negativo, `0` se
  não tem). Salvaguarda segue o mesmo trio. Os `*_flag`, o `npc_skills_flag` e o
  `npc_saving_flag` **não estão em `npc_attrs`** — não saem no export e vão à
  mão, como o `atkattr_base` do PC; sem eles a linha inteira de perícias some.
- **NPC não tem campo de passiva nem de iniciativa própria**: a passive
  Perception vai como texto dentro de `npc_senses`, e a iniciativa sai de
  `initiative_bonus` com `init_tiebreaker: "@{dexterity}/100"`.
- **`rtype` sem `selected` no HTML cai em "Always Roll Advantage"** — a primeira
  option do select. Gravar `@{advantagetoggle}`, cujo default já vem embutido no
  atributo, ou toda rolagem da ficha sai com vantagem.
- No `repeating_npcaction`, `attack_flag` é `"on"` (o worker só testa `!= "0"`),
  `show_desc` é literalmente `"@{description}"`, e o `rollbase` do ramo de ataque
  é o template `npcatk` com os links `~repeating_npcaction_npc_dmg`/`_npc_crit`.

Aprendido na evolução do Kael para o 3º nível (2026-09-05), partindo do **export do
Jogador** em vez de gerar do zero — o export preserva o estado de jogo, e o script
só aplica o delta da ficha do repo:

- O HTML do sheet baixa direto com `curl` de
  `https://raw.githubusercontent.com/Roll20/roll20-character-sheets/master/StarWars5E/StarWars5E_HTML.html`
  (~1 MB); grepar `name="attr_..."` dá os 617 nomes de campo e as options dos selects.
- **Arquétipo** é `subclass`, input de texto livre; não sai no export quando vazio.
- `atkattr_base` do ataque de poder é literalmente `power` (as outras options são
  `@{<atributo>_mod}` e `0`). Concentração num poder é `powerconcentration:
  "{{concentration=1}}"` (senão `"0"`). Expertise de ferramenta é
  `toolbonus_base: "(@{pb}*2)"`, com `toolbonus` já somado.
- **Flags de perícia e salvaguarda de NPC**: o worker processa em ordem alfabética
  **inversa**, e a primeira processada leva flag `2` — ou seja, `2` vai na perícia
  alfabeticamente **última** entre as que têm valor (`4` se negativa), `1` nas
  outras (`3` se negativa), `0` nas sem valor. Nas salvaguardas a ordem de
  processamento é cha, wis, int, con, dex, str. `npc_skills_flag` e
  `npc_saving_flag` são só a concatenação dos valores, servem como "não vazio".
- NPC conjurador: `npcpowercastingflag: "1"`, `powercasting_ability`,
  `power_save_dc`, `power_attack_bonus`, e os poderes nas mesmas
  `repeating_power-*` do PC. Ação de NPC sem ataque usa
  `rollbase: "@{wtype}&{template:npcaction} @{npc_name_flag} {{rname=@{name}}} {{description=@{show_desc}}} @{charname_output}"`.
- Estado que se preserva do export: PV corrente vira `corrente + (novo máximo −
  máximo antigo)`; `tech_power_points_expended` (que é *remaining*) idem;
  `inspiration`, `class_resource` corrente e `rtype` ficam como o Jogador deixou.
- Os JSONs gerados vivem em `tmp/` do repo, que está no `.gitignore` — nunca
  commitados, como manda a regra da harness.

A conversão da ficha do Kael foi gerada por script descartável (morreu no chat, como
manda a regra); o JSON entregue ao Jogador não vira arquivo do repo.
