# SW5e Harness

Harness em arquivos (AGENTS.md, skills, memória) que ajuda Arthur a criar personagens e NPCs de Star Wars 5e com ficha completa, acumulando o contexto de cada mesa entre sessões. Ele é jogador numa campanha e mestre em outra.

O ponto do projeto é o contexto de campanha: o agente conhece a mesa sem que ela precise ser recontada a cada conversa.

## Language

### Pessoas e papéis

**Jogador**:
O usuário da harness (Arthur). Dono do conceito e do rumo de cada personagem. Joga como jogador numa mesa e como mestre em outra — a harness serve aos dois papéis.
_Avoid_: usuário, mestre (o papel varia por campanha)

**Agente**:
O agente de IA que executa a harness. Pergunta pouco, monta a ficha consultando o Espelho, confere e grava.

### Campanha

**Campanha**:
Uma mesa, materializada como subpasta de `campanhas/` com Contexto, Crônica e as fichas de PCs, NPCs e inimigos. Registrada no `CONTEXT-MAP.md` da raiz.
_Avoid_: mesa (na conversa é sinônimo; como termo de arquivo, use Campanha)

**Contexto da campanha**:
O `CONTEXT.md` de uma Campanha: o que é verdade **agora** — era, tom, nível do grupo, método de atributos, fontes permitidas, quem é o grupo, facções relevantes e casa-regras. Lido inteiro antes de toda ficha, então precisa caber numa tela.
_Avoid_: descrição da campanha, lore

**Crônica**:
O `CRONICA.md` de uma Campanha: histórico append-only, uma entrada por sessão. Cresce sem culpa porque quase nunca é lida inteira — só a cauda. É o que faz um NPC ficar interessante depois, porque guarda o que aconteceu.
_Avoid_: log, histórico, timeline

**Promoção**:
Mover para o Contexto da campanha algo que a sessão tornou estado permanente (facção que virou hostil, NPC que morreu, casa-regra fixada). O resto fica só na Crônica. Na dúvida, não promove.

**Divergência do cânon**:
Onde a mesa contraria ou inventa sobre o Star Wars conhecido. É a única parte do cânon que vira arquivo — o resto o Agente já sabe, e anotá-lo é manutenção sem retorno.

### Ficha

**Ficha canônica**:
O JSON do esquema `sw5e-ficha/1` que descreve um personagem por inteiro: identidade, narrativa, build, atributos, derivados, proficiências, poderes, equipamento, ataques, features e fontes. É a saída do projeto e é **genérica**: nenhum campo existe por causa de um VTT.
_Avoid_: ficha do Roll20, sheet

**PC**:
Personagem do Jogador. Vive em `campanhas/<slug>/personagens/`.

**NPC**:
Personagem não-jogador — aliado, contato, tripulação. Vive em `campanhas/<slug>/npcs/`. Usa a Ficha canônica com `"tipo": "npc"` e narrativa enxuta.

**Inimigo**:
NPC adversário. Mesmo esquema, pasta `inimigos/`. A distinção é de intenção, não de mecânica.

**Seed**:
A frase com que o Jogador abre um pedido de ficha ("um bothan spy que trai o grupo"). O Agente completa o resto perguntando só o que trava.

**Derivados**:
Os valores calculados da ficha — modificadores, bônus de proficiência, PV, CA, iniciativa, salvaguardas, perícias, DC de poder, bônus de ataque. Gravados na ficha e conferidos pelo Agente antes de gravar.

### Espelho

**Espelho**:
A cópia local do conteúdo de SW5e em `sw5e/`, sincronizada da API pública da comunidade. É a fonte de verdade de conteúdo: o que não está nele não existe.
_Avoid_: base de dados, cache

**Fatia**:
Um arquivo do Espelho, uma entidade por arquivo (uma espécie, um poder, um monstro). Lida sob demanda.

**Índice**:
O `INDEX.md` de uma coleção do Espelho: nome e uma linha por entidade. O Agente escolhe pelo Índice e só então abre a Fatia — a coleção inteira custa quase mil vezes mais.

**Sync**:
A execução de `tools/sync-espelho.py`, que rebaixa a API e reescreve Fatias e Índices. Sob demanda, quando a comunidade atualiza conteúdo.

### Conferência

**Conferência**:
O que o Agente faz sobre uma Ficha canônica antes de gravar, em criação e em evolução: **esquema** (as chaves e os tipos de `sw5e-ficha/1`), **aritmética** (os Derivados fecham) e **Legalidade**. Ficha que não fecha não é gravada.
_Avoid_: validação, validar (nomeiam uma ferramenta que não existe — quem confere é o Agente)

**Legalidade**:
A ficha ser permitida pelas regras e pelo conteúdo existente: toda entidade nomeada existe como Fatia do Espelho, o nível do poder é acessível, o pré-requisito confere. Não é juízo de qualidade — se a build é boa é julgamento do Agente, e a Conferência não opina.
