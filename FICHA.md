# `sw5e-ficha/1` — o esquema da Ficha canônica

A saída do projeto. Um JSON por personagem, em `campanhas/<slug>/personagens/`,
`npcs/` ou `inimigos/`, com o nome do personagem em slug
(`Vessa Korr` → `vessa-korr.json`).

Leia este arquivo antes de escrever ou editar uma ficha. Ele não repete as regras
duras do `AGENTS.md` — só diz o que cada campo é, e o que o Espelho ensinou sobre
como preenchê-lo.

## Os três princípios

**A ficha guarda a escolha; a regra fica no Espelho.** O que só a ficha sabe é o
que foi escolhido — esta espécie, esta perícia, este poder, este exploit, este
+2 de atributo. O texto da regra não se copia para cá: ele está na Fatia, e o
`fontes` diz em qual.

**Todo número da ficha é máximo, nunca corrente.** `pv` é o total; `Force Points`
é a reserva cheia. PV perdido, ponto gasto, carga de célula e crédito no bolso
são estado de mesa e não entram — não há nada aqui que os atualize.

**Inglês significa "existe no Espelho".** Todo nome em inglês tem que estar no
Espelho: como Fatia — e então tem linha em `fontes` — ou como prosa dentro de uma
Fatia, e então quem aponta para ela é o `origem` da feature. Nome em PT-BR é o
contrário: não existe no Espelho, e por isso **não pode carregar mecânica**. A
cópia de uma carta estelar entra em PT-BR; uma arma, nunca.

## O esquema

| Campo | pc | npc | O que é |
| --- | --- | --- | --- |
| `esquema` | obr. | obr. | `"sw5e-ficha/1"` |
| `tipo` | obr. | obr. | `"pc"` ou `"npc"` — aliado ou adversário é a pasta que diz, não este campo |
| `campanha` | obr. | obr. | slug da Campanha |
| `base` | — | opc. | Fatia de monstro de onde o NPC partiu (`sw5e/monstros/<slug>.json`) |
| `identidade` | obr. | obr. | `nome`, `especie`, `idade`, `alinhamento`, `aparencia` |
| `narrativa` | obr. | enxuta | `conceito`, `tracos`, `ideais`, `vinculos`, `fraquezas`, `historia`, `ganchos` |
| `build` | obr. | opc. | `nivel`, `classes[]` (`classe`, `nivel`, `arquetipo`), `background`, `feats[]` |
| `atributos` | obr. | obr. | os seis valores **finais** |
| `derivados` | obr. | obr. | ver abaixo |
| `recursos` | cond. | cond. | os recursos de classe deste nível |
| `proficiencias` | obr. | parcial | `salvaguardas`, `pericias`, `expertise`, `armas`, `armaduras`, `ferramentas`, `idiomas` |
| `poderes` | cond. | cond. | `forca[]`, `tech[]` |
| `equipamento` | obr. | obr. | `itens[]` com `nome` e `qtd` |
| `ataques` | obr. | obr. | `nome`, `bonus`, `dano`, `tipo`, `alcance` |
| `features` | obr. | obr. | o rol completo do que foi ganho |
| `fontes` | obr. | obr. | nome → caminho da Fatia |
| `notas` | opc. | opc. | o que a aritmética não explica sozinha |

**Chave é PT-BR. Valor que nomeia entidade é inglês**, com a capitalização e a
pontuação da Fatia: `"Combat suit"` (não `Combat Suit`), `"Clothes, common"`
(não `Common Clothes`), `"Blaster pistol"`, `"Mechanic's kit"`. Corrigir o nome
quebra a busca.

**Campo condicional é omitido quando o Espelho prova que não se aplica.**
`poderes` existe se a classe **ou o arquétipo** conjurar — e é o arquétipo que
decide com frequência: `Beguiler Practice` faz um Operative, classe sem
conjuração, virar caster de Força. Dentro de `poderes`, `tech` sai se não houver
poder tech. `recursos` existe se a tabela de nível der algo além de nível, bônus
de proficiência e features — o que hoje vale para as 10 classes.

### `atributos`

Os seis nomes em inglês (`Strength`, `Dexterity`, `Constitution`,
`Intelligence`, `Wisdom`, `Charisma`), como no `savingThrows` das classes — a
mesma grafia aqui e lá, para copiar sem traduzir.

**Os valores são finais**: o aumento da espécie, o do feat e o ASI já estão
dentro. Cuidado com feat que sobe atributo — `Ace Pilot` tem
`attributesIncreased: ["Intelligence"]` e dá `+1 Intelligence` **além** da
proficiência em Piloting. O método de geração não entra: ele é fato da Campanha
e está no Contexto dela.

### `derivados`

`modificadores` (os seis, mesmos nomes), `bonusProficiencia`, `pv` (máximo),
`ca`, `iniciativa`, `deslocamento` **em pés**, e — se conjurar — `dcPoder` e
`bonusAtaquePoder`.

Esses dois são **número ou objeto por alinhamento**. Número quando a habilidade
de conjuração é uma só. Objeto quando o Espelho manda variar: o
`Beguiler Practice` usa Wisdom para poder `Light`, Charisma para `Dark`, e a
escolha do jogador para `Universal` — três DCs possíveis, então as chaves são os
valores de `forceAlignment` da Fatia do poder. Grave só os alinhamentos que a
lista de poderes usa.

### `recursos`

Um mapa cujas **chaves são as colunas da tabela de nível**, exatamente como o
Espelho as escreve: `Sneak Attack`, `Force Points`, `Max Power Level`, `Rages`,
`Rage Damage`, `Superiority Dice Quantity`, `Aura Radius`, `Martial Arts`… São 31
colunas distintas nas 10 classes e só três são comuns a todas, então não existe
lista fixa de derivado que caiba nisto — o que cabe é a coluna da classe deste
personagem.

Quatro regras de leitura da tabela:

- **Valor efetivo, não cópia.** A coluna é a fonte, não a resposta: a Fatia do
  `Beguiler Practice` manda somar ao Force Points da tabela um modificador de
  atributo. A tabela dá 4 no nível 4, e a ficha do exemplo grava 7 — leia a
  Fatia, não confie na coluna sozinha.
- **Some classe e arquétipo.** Os dois têm tabela própria, e um Operative
  Beguiler tem `Sneak Attack` da classe e `Force Points` do arquétipo.
  Multiclasse que repete a coluna grava o total efetivo, e o `notas` explica.
- **Coluna `*Known` não entra** quando a lista correspondente já está na ficha —
  `Force Powers Known` é o tamanho de `poderes.forca`. E é exatamente o tamanho:
  ver `poderes`, abaixo.
- **`�` quer dizer "nada neste nível"**, não conteúdo. A API perdeu travessões
  na origem, e `Operative Exploits: "�"` no nível 1 é uma coluna que ainda não
  vale — não copie.

`Max Power Level` é a única normalização: a tabela escreve `"1st"`, a ficha grava
`1`, porque é com o `level` inteiro da Fatia do poder que ele se compara.

### `poderes`

`forca[]` e `tech[]` guardam os poderes **escolhidos** — os que a coluna `*Known`
da tabela conta. Por isso a lista tem o tamanho exato da coluna, e é isso que
torna a evolução mecânica: a coluna sobe, e a diferença é quanto se escolhe.

**Poder concedido não entra aqui.** Espécie e arquétipo dão poder de graça — o
Miraluka já nasce com `Mind Trick` e ganha `Sanctuary` no 3º —, e poder concedido
não é escolha: ele é derivável da entidade que o deu. Quem o nomeia é o `resumo`
da feature que o concede, e ele tem linha em `fontes` como qualquer outro nome em
inglês. Somá-lo à lista faria a conta com a coluna parar de fechar e duplicaria o
Espelho dentro da ficha.

A ficha então não tem uma lista só do que o personagem conjura — quem monta isso
é o Agente, ao fechar a conversa. `notas` é onde se diz que existe concedido.

### `proficiencias`

`salvaguardas` e `pericias` usam os nomes em inglês das Fatias
(`Piloting`, `Technology`, `Lore` — SW5e não tem Arcana nem History).
**Perícia e idioma não são coleções do Espelho**: só existem como prosa dentro de
Fatias, então não têm linha em `fontes` e a conferência é achar o nome na prosa
que os concede.

`expertise` é a lista de proficiências com bônus dobrado — é aqui que a escolha
de `Expertise` mora, não em `features`.

`armas` pede cuidado: a API quebra a frase da classe em vírgulas, e o
`weaponProficiencies` do Operative sai como `[…, "special", "strength", "and
two-handed properties"]`. São fragmentos de uma frase só. **Remonte a frase**
antes de gravar.

`ferramentas` mistura o que tem Fatia (`Security kit`) com o que não tem: SW5e
não tem instrumento musical nem mochila de aventureiro como entidade, embora
classe e espécie os concedam. O que não tem Fatia entra em PT-BR.

### `features`

O **rol completo** do que o personagem ganhou, cada entrada com `nome`, `origem`
e `resumo` de uma linha — e `escolha` quando a feature escolheu algo que não tem
campo próprio. `origem` é a entidade mais o nível em que veio: `"Operative 4"`,
`"Beguiler Practice 3"`, `"Bith"`, `"Spacer"`.

Ser o rol completo é o que deixa a evolução mecânica: comparar a coluna
`Features` da próxima linha da tabela com esta lista mostra o que falta ganhar.

Não entra a feature cujo conteúdo **inteiro** já está gravado em outro campo:
`Operative Practice` é o `arquetipo`, `Forcecasting` é o bloco de conjuração,
`Ace Pilot` é o `feats`. `Ability Score Improvement` **entra**, porque só a
`escolha` dela registra quais atributos subiram — do valor final não se recupera.

Nunca a prosa da regra: `classFeatureText` tem 16 KB no Operative e ele está no
Espelho, a uma linha de `fontes` de distância.

### `fontes`

Nome da entidade → caminho da Fatia, para tudo que a ficha nomeia nas nove
coleções. É o **recibo da Conferência de Legalidade**: quem escreveu a ficha
provou que cada nome existe, e quem a reabre daqui a meses reabre a origem de
cada escolha sem adivinhar.

Não é derivável, e é por isso que existe: o slug engole apóstrofo e vírgula
(`Mechanic's kit` → `mechanic-s-kit.json`, `Clothes, common` →
`clothes-common.json`) e seis Fatias têm nome de arquivo com discriminador
(`bo-rifle-exoticblaster.json`). **Nome em inglês sem linha em `fontes` é nome
não conferido.**

## Exemplo — PC completo

Vessa Korr, nível 4, na mesa fictícia que a skill `nova-campanha` usa de
exemplo. É exemplo: nenhuma Campanha com este slug existe no repo.

```json
{
  "esquema": "sw5e-ficha/1",
  "tipo": "pc",
  "campanha": "sombras-de-ord-mantell",
  "identidade": {
    "nome": "Vessa Korr",
    "especie": "Bith",
    "idade": 34,
    "alinhamento": "neutra e equilibrada",
    "aparencia": "Crânio alto e pele esverdeada, dedos longos manchados de tinta de carta estelar. Casaco de piloto dois números maior que o dela, com o brasão arrancado."
  },
  "narrativa": {
    "conceito": "Cartógrafa de rotas que vendeu ao cartel um mapa que não fechava e agora paga a diferença em serviço.",
    "tracos": [
      "Mede tudo em horas de salto, inclusive conversa.",
      "Fala pouco e repete depois o que ninguém queria ter dito."
    ],
    "ideais": ["Rota trancada não vale nada. Informação existe para circular."],
    "vinculos": ["O hiperdrive remendado da Hollow Coin é culpa dela, e Talon nunca cobrou."],
    "fraquezas": ["Não admite erro de cálculo: prefere refazer o trajeto inteiro a corrigir uma linha."],
    "historia": "Passou doze anos vendendo cartas de hiperrota para quem não podia usar as oficiais. O mapa que vendeu ao comprador do cartel tinha um salto a menos, e a carga inteira ficou parada em Ord Mantell — prejuízo que virou 40.000 créditos no nome dela e dos dois que estavam na nave.",
    "ganchos": [
      "O comprador ainda não sabe quem assinou a carta errada.",
      "Guarda a cópia original, e nela existe uma rota que o cartel jura não existir."
    ]
  },
  "build": {
    "nivel": 4,
    "classes": [{ "classe": "Operative", "nivel": 4, "arquetipo": "Beguiler Practice" }],
    "background": "Spacer",
    "feats": ["Ace Pilot"]
  },
  "atributos": {
    "Strength": 8,
    "Dexterity": 16,
    "Constitution": 12,
    "Intelligence": 16,
    "Wisdom": 10,
    "Charisma": 16
  },
  "derivados": {
    "modificadores": {
      "Strength": -1,
      "Dexterity": 3,
      "Constitution": 1,
      "Intelligence": 3,
      "Wisdom": 0,
      "Charisma": 3
    },
    "bonusProficiencia": 2,
    "pv": 27,
    "ca": 14,
    "iniciativa": 3,
    "deslocamento": 30,
    "dcPoder": { "Dark": 13, "Universal": 13 },
    "bonusAtaquePoder": { "Dark": 5, "Universal": 5 }
  },
  "recursos": {
    "Sneak Attack": "2d6",
    "Operative Exploits": 2,
    "Force Points": 7,
    "Max Power Level": 1
  },
  "proficiencias": {
    "salvaguardas": ["Dexterity", "Intelligence"],
    "pericias": [
      "Deception",
      "Insight",
      "Investigation",
      "Perception",
      "Persuasion",
      "Piloting",
      "Stealth",
      "Technology"
    ],
    "expertise": ["Deception", "Piloting"],
    "armas": [
      "Simple blasters",
      "Simple vibroweapons",
      "Martial blasters that lack the auto, special, strength, and two-handed properties",
      "Martial vibroweapons with the finesse property"
    ],
    "armaduras": ["Light armor"],
    "ferramentas": ["Security kit", "Mechanic's kit", "Slicer's kit", "instrumento musical (valachord)"],
    "idiomas": ["Galactic Basic", "Bith", "Huttese", "Binary"]
  },
  "poderes": {
    "forca": ["Denounce", "Force Disarm", "Hex", "Mind Trick", "Sense Force", "Slow"]
  },
  "equipamento": {
    "itens": [
      { "nome": "Combat suit", "qtd": 1 },
      { "nome": "Vibrodagger", "qtd": 1 },
      { "nome": "Blaster pistol", "qtd": 1 },
      { "nome": "Power cell", "qtd": 2 },
      { "nome": "Clothes, common", "qtd": 1 },
      { "nome": "Security kit", "qtd": 1 },
      { "nome": "Mechanic's kit", "qtd": 1 },
      { "nome": "Slicer's kit", "qtd": 1 },
      { "nome": "cópia da carta estelar que ela vendeu ao cartel", "qtd": 1 }
    ]
  },
  "ataques": [
    {
      "nome": "Vibrodagger",
      "bonus": 5,
      "dano": "1d4+3",
      "tipo": "Kinetic",
      "alcance": "corpo a corpo, ou arremesso 20/60"
    },
    {
      "nome": "Blaster pistol",
      "bonus": 5,
      "dano": "1d6+3",
      "tipo": "Energy",
      "alcance": "50/200, reload 16"
    }
  ],
  "features": [
    { "nome": "Detail Oriented", "origem": "Bith", "resumo": "vantagem em Investigation a até 5 pés" },
    { "nome": "Keen Hearing and Smell", "origem": "Bith", "resumo": "vantagem em Perception de audição ou olfato" },
    { "nome": "Musician", "origem": "Bith", "resumo": "proficiência em um instrumento musical" },
    { "nome": "Programmer", "origem": "Bith", "resumo": "expertise em Technology quando o teste envolve computador" },
    { "nome": "Sonic Sensitivity", "origem": "Bith", "resumo": "desvantagem contra efeito sonoro ensurdecedor" },
    { "nome": "Trance", "origem": "Bith", "resumo": "descanso longo com 3 h de sono" },
    { "nome": "Expertise", "origem": "Operative 1", "resumo": "dobra o bônus de duas proficiências" },
    { "nome": "Sneak Attack", "origem": "Operative 1", "resumo": "dano extra com finesse ou à distância, com vantagem ou aliado adjacente" },
    { "nome": "Cunning Action", "origem": "Operative 2", "resumo": "Dash, Disengage ou Hide como ação bônus" },
    {
      "nome": "Operative Exploits",
      "origem": "Operative 2",
      "resumo": "dois exploits adotados",
      "escolha": ["Explorer's Exploit", "Learner's Exploit"]
    },
    { "nome": "Bad Feeling", "origem": "Operative 3", "resumo": "move-se até o deslocamento antes de rolar iniciativa, 1x por descanso longo" },
    {
      "nome": "Ability Score Improvement",
      "origem": "Operative 4",
      "resumo": "aumento de atributo",
      "escolha": "+2 Charisma"
    },
    { "nome": "Fascinating Display", "origem": "Beguiler Practice 3", "resumo": "1 min de exibição charma humanoides que assistiram, DC 13" },
    { "nome": "Well-Traveled", "origem": "Spacer", "resumo": "conhecimento de hiperrota segura e de modelo de nave comum" }
  ],
  "fontes": {
    "Bith": "sw5e/especies/bith.json",
    "Operative": "sw5e/classes/operative.json",
    "Beguiler Practice": "sw5e/arquetipos/beguiler-practice.json",
    "Spacer": "sw5e/backgrounds/spacer.json",
    "Ace Pilot": "sw5e/feats/ace-pilot.json",
    "Denounce": "sw5e/poderes/denounce.json",
    "Force Disarm": "sw5e/poderes/force-disarm.json",
    "Hex": "sw5e/poderes/hex.json",
    "Mind Trick": "sw5e/poderes/mind-trick.json",
    "Sense Force": "sw5e/poderes/sense-force.json",
    "Slow": "sw5e/poderes/slow.json",
    "Combat suit": "sw5e/equipamentos/combat-suit.json",
    "Vibrodagger": "sw5e/equipamentos/vibrodagger.json",
    "Blaster pistol": "sw5e/equipamentos/blaster-pistol.json",
    "Power cell": "sw5e/equipamentos/power-cell.json",
    "Clothes, common": "sw5e/equipamentos/clothes-common.json",
    "Security kit": "sw5e/equipamentos/security-kit.json",
    "Mechanic's kit": "sw5e/equipamentos/mechanic-s-kit.json",
    "Slicer's kit": "sw5e/equipamentos/slicer-s-kit.json"
  },
  "notas": "Force Points = 4 (tabela do Beguiler Practice no nível 4) + 3 (Charisma, escolhida em vez de Wisdom); a mesma escolha fixa o DC e o bônus de ataque dos poderes Universal. Sem poder Light na lista, não há DC de Light gravado. A casa-regra de descanso longo desta mesa (8 h em doca segura) encurta o ganho do Trance."
}
```

## Exemplo — NPC, o que muda

Recorte: **só as chaves que o NPC usa de outro jeito.** O resto é igual ao
exemplo acima — é o mesmo esquema.

```json
{
  "tipo": "npc",
  "base": "sw5e/monstros/inquisitor-knight.json",
  "identidade": {
    "nome": "Inquisidora Vahl",
    "especie": "Human",
    "alinhamento": "leal e sombria"
  },
  "narrativa": {
    "conceito": "Remanescente do Império que compra do cartel a localização de sensitivos e cobra em serviço prestado.",
    "ganchos": ["Sabe que alguém em Ord Mantell vendeu uma rota que ela usou."]
  },
  "derivados": {
    "bonusProficiencia": 2,
    "pv": 36,
    "ca": 15,
    "iniciativa": 3,
    "deslocamento": 30,
    "dcPoder": 13,
    "bonusAtaquePoder": 5
  },
  "recursos": { "Force Points": 18, "Max Power Level": 2 },
  "poderes": {
    "forca": [
      "Denounce",
      "Force Disarm",
      "Saber Throw",
      "Slow",
      "Dark Side Tendrils",
      "Fear",
      "Force Jump",
      "Hex",
      "Sense Force",
      "Force Sight",
      "Stun"
    ]
  },
  "ataques": [
    { "nome": "Doublesaber", "bonus": 5, "dano": "1d8+3", "tipo": "Energy", "alcance": "corpo a corpo, 5 pés" },
    { "nome": "Spinning Doublesaber", "bonus": 5, "dano": "2d8+3", "tipo": "Energy", "alcance": "corpo a corpo, 5 pés" }
  ],
  "features": [
    { "nome": "Force Resistance", "origem": "base", "resumo": "vantagem em salvaguardas contra poderes de Força" },
    { "nome": "War Casting", "origem": "base", "resumo": "ataque de Doublesaber como ação bônus depois de conjurar" }
  ],
  "notas": "O bloco veste \"heavy combat suit\", nome que não é Fatia; adotada a Durafiber battle armor, armadura pesada de CA fixa 15, para o número fechar com o base. Max Power Level 2 lido do maior nível de poder que o bloco lista."
}
```

Cinco coisas mudam num NPC de base de monstro:

- **`base`** aponta a Fatia do monstro. É o recibo dos números copiados e o
  lugar onde ficam senses, imunidades, resistências e desafio — nada disso vira
  campo aqui.
- **`build` sai**: não há nível de classe. O bloco é a build.
- **`recursos` vem da prosa do bloco**, não de tabela de nível — este é um
  forcecaster de 5º nível com 18 Force Points escritos no `behaviors`.
- **`narrativa` é enxuta**: conceito e gancho. Traço, ideal, vínculo e fraqueza
  são do PC.
- **`proficiencias` fica parcial**: salvaguardas, perícias e idiomas, que o bloco
  dá. Arma, armadura e ferramenta não, porque os ataques já vêm resolvidos.

`origem: "base"` é a única forma de origem que não nomeia entidade: quem aponta é
o campo `base`.

A ficha vira PC ao contrário quando o NPC é construído com níveis: aí ele tem
`build`, não tem `base`, e é uma ficha comum com `"tipo": "npc"`.

## Conferência, campo por campo

Antes de gravar, além do que o `AGENTS.md` já manda:

1. **Nome em inglês tem linha em `fontes`** e o arquivo existe — ou o nome está
   na prosa da Fatia que o `origem` aponta (exploit, maneuver, fighting style).
   Nome em PT-BR não carrega mecânica.
2. **Atributo final confere** com base + espécie + feat + ASI, e nenhum passa de
   20.
3. **`modificadores`, `bonusProficiencia`, `pv`, `ca`, `iniciativa` fecham** — CA
   pela string `ac` da armadura, PV pelos números de dado de vida da classe.
4. **Ataque fecha** com a Fatia da arma: dado, `damageType` e propriedade
   (finesse decide se o bônus é de Dexterity ou Strength).
5. **`recursos` é a linha certa da tabela** — nível certo, classe **e**
   arquétipo, valor efetivo.
6. **Poder cabe no `Max Power Level`**, a lista tem o tamanho exato da coluna
   `*Known`, e todo poder concedido está fora dela e nomeado na feature que o
   concede.
7. **Cada proficiência tem quem a concedeu**, e a mesma não foi concedida duas
   vezes por fontes diferentes — ou, se foi, a Fatia diz no que a segunda vira
   (o `Loremaster` troca proficiência repetida em `Lore` por expertise).
8. **`features` cobre a coluna `Features` de todas as linhas até o nível atual.**
