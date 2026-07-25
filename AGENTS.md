# AGENTS.md — sw5e-harness

Workspace de criação de personagens e NPCs de **Star Wars 5e**. O Jogador conduz; o agente pergunta pouco, monta a ficha, confere e grava. O vocabulário desta ferramenta vive em `CONTEXT.md` (raiz) — use-o com precisão.

## Papéis

- O **Jogador** (Arthur) é jogador numa mesa e mestre em outra. Ele decide conceito e rumo; o agente cuida de regra, aritmética e arquivos.
- O agente **não pergunta o que já está registrado no contexto da campanha**. Repetir pergunta que a mesa já respondeu é o defeito que esta harness existe para não ter.
- Tudo que não é conceito é do agente: julgamento de build (o personagem é bom? é interessante?), legalidade e aritmética. Não há ferramenta que confira ficha — a responsabilidade é sua e não passa para ninguém.

## Layout

| Caminho | O que é |
| --- | --- |
| `CONTEXT.md` | Vocabulário da harness |
| `CONTEXT-MAP.md` | Mapa das campanhas |
| `FICHA.md` | O esquema `sw5e-ficha/1`, campo por campo, com exemplo — leia antes de escrever ficha |
| `sw5e/` | Espelho de regras: uma fatia por entidade, mais `INDEX.md` por coleção |
| `campanhas/<slug>/CONTEXT.md` | Estado da mesa |
| `campanhas/<slug>/CRONICA.md` | Histórico da mesa, append-only |
| `campanhas/<slug>/personagens/` | PCs do Jogador |
| `campanhas/<slug>/npcs/` | Aliados, contatos, tripulação |
| `campanhas/<slug>/inimigos/` | Adversários |
| `tools/` | `sync-espelho.py`, o único artefato de código do repo |
| `.agents/memory/` | Memória do workspace (índice em `MEMORY.md`) |
| `.agents/skills/` | Skills deste workspace |

## Ritual de abertura

1. Identifique a campanha. Se o Jogador não nomear e houver mais de uma no `CONTEXT-MAP.md`, pergunte — é a única pergunta que vale fazer antes de ler qualquer coisa.
2. Leia o `CONTEXT.md` da campanha **inteiro** e as últimas entradas da `CRONICA.md`.
3. Responda em uma ou duas linhas dizendo onde a mesa está e o que ele quer fazer. Nada de relatório.

## Regras duras

**A harness não é software.** É harness de jogo de interpretação: o que ela tem de valioso é contexto e disciplina, não código. Você lê, entende, procura no espelho e — se ajudar a fechar os números de uma ficha — **escreve um script na hora**. Esse script morre no chat: não vai para `tools/`, não é commitado, não vira dependência da próxima conversa. `sync-espelho.py` é a única exceção, e ela já está tomada.

**A saída é genérica.** A ficha canônica é o JSON do esquema `sw5e-ficha/1`, documentado em `FICHA.md` — leia-o antes de escrever ou editar ficha, e não pertence a nenhum VTT. Converter para o formato do Roll20 ou de outro tabletop é tarefa de conversa, feita na hora e entregue no chat — **nunca vira arquivo do repo**. O Jogador pode trocar de VTT, e um renderizador acoplado viraria dívida no dia seguinte.

**Ficha que não fecha não é gravada.** Antes de escrever qualquer ficha, em criação e em evolução, confira você mesmo: toda entidade nomeada existe como fatia no espelho, os derivados fecham, as chaves e os tipos são os do esquema. Se não fechar, corrija e confira de novo. Não grave "para arrumar depois" — não há ferramenta para pegar isso depois.

**O espelho é a fonte de conteúdo.** Espécie, classe, arquétipo, background, poder, feat e item vêm de `sw5e/`. Escolha lendo o `INDEX.md` da coleção e só então abra a fatia — abrir a coleção inteira custa quase mil vezes mais e não é necessário. Conteúdo de SW5e que você "lembra" mas não está no espelho **não existe**.

O arquivo da fatia é o nome da entidade em slug (`Bo-rifle` → `bo-rifle.json`). Onde dois nomes colidem, o índice traz o arquivo entre backticks na linha — são poucos casos, e o índice é quem manda. A fatia não é cópia crua da API: saem dela as duplicações do mesmo dado e o plumbing de armazenamento, e nada mais.

**Cânon não vira arquivo.** A era, os planetas e as facções do Star Wars você já conhece. O `CONTEXT.md` da campanha registra apenas onde a mesa **diverge** do cânon ou o que ela inventou.

**Estado e histórico são coisas diferentes.** `CONTEXT.md` é o que é verdade agora e é lido inteiro antes de toda ficha, então tem que ficar pequeno. `CRONICA.md` é append-only e quase nunca é lido inteiro. Ao registrar uma sessão, promova ao `CONTEXT.md` só o que virou estado permanente; na dúvida, não promova.

**Nomes de entidade ficam em inglês.** A conversa é em PT-BR, mas todo valor que nomeia uma entidade do espelho — espécie, classe, arquétipo, background, perícia, poder, item — é gravado com o nome original, exatamente como no espelho, ou a busca para de casar. Texto livre, alinhamento, alcance e aparência ficam em PT-BR.

## Skills

Vivem em `.agents/skills/<nome>/SKILL.md`. As regras acima valem para todas e **não se repetem dentro delas**: uma skill diz apenas qual contexto ler, o que perguntar e onde escrever.

| Skill | Quando |
| --- | --- |
| `nova-campanha` | "Vou entrar numa mesa nova", "vou mestrar uma campanha" |
| `criar-personagem` | Um PC do Jogador |
| `criar-npc` | Um NPC, aliado ou inimigo |
| `registrar-sessao` | "Joguei ontem", "registra a sessão" |
| `evoluir-personagem` | "Subi de nível" — a partir da ficha guardada, com o que mudou na mesa entrando falando |

## Ferramentas

`python3 tools/sync-espelho.py` sincroniza o espelho com a API pública do sw5e. Rodado sob demanda, quando a comunidade atualiza conteúdo — não é ritual de sessão.

É a única ferramenta do repo, em Python 3 stdlib puro, sem dependência externa. Mantenha assim, e não acrescente outra.

## Regras gerais

- Idioma da conversa: **PT-BR**.
- Commits sem trailer de coautoria.
- Descoberta operacional durável vira memória em `.agents/memory/`, não comentário em arquivo.

## Estado atual

O esqueleto está de pé; o resto está em construção, rastreado no mapa `.scratch/sw5e-harness/map.md` e nos tickets em `.scratch/sw5e-harness/issues/`, na raiz do workspace (`/root/projetos`).

Já existem: o espelho `sw5e/` com as 3.629 fatias e os nove índices, e o `tools/sync-espelho.py` que o produz (issue 03); o esquema `sw5e-ficha/1` em `FICHA.md` (issue 04).

Ainda **não existem**: quatro das cinco skills — só `nova-campanha` está escrita (issue 05); faltam as outras (issues 06 e 07). Até cada uma chegar, as regras acima descrevem o alvo, não o presente — não finja que a peça existe. Nenhuma ficha foi escrita ainda: o exemplo do `FICHA.md` é exemplo, e a mesa dele não existe como Campanha.

Apague esta seção quando a issue 07 fechar.
