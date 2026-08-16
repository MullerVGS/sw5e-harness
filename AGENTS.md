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

**O espelho é atalho, não fronteira.** Ele existe para uma coisa: fazer a escolha ser rápida e a grafia exata. Tudo que a ficha escolhe vem de `sw5e/`: espécie, classe, arquétipo, background, poder, feat, item, perícia e as escolhas de combate — manobra, fighting style, fighting mastery, forma de sabre, weapon focus, weapon supremacy. Escolha lendo o `INDEX.md` da coleção e só então abra a fatia — abrir a coleção inteira custa quase mil vezes mais e não é necessário. Nome que a ficha grava tem que casar com uma fatia; escolha que você "lembra" mas não tem fatia não entra na ficha.

**Regra e minúcia se pesquisam.** O espelho não guarda os capítulos de regra, e isso é de propósito — não é licença para inventar nem motivo para parar e devolver a dúvida ao Jogador. Ir atrás é seu trabalho, na ordem do custo: o que você sabe de 5e vale como ponto de partida, porque SW5e é 5e com outra pele; a memória do workspace guarda o que já foi pesquisado; os dois livros estão na API — `https://sw5eapi.azurewebsites.net/api/playerHandbookRule` e `/api/wretchedHivesRule`, coleção inteira, um capítulo por entidade: baixe e filtre com script descartável; o resto está na web, onde o documento de Companions vive em GMBinder. O site sw5e.com é SPA e não responde a fetch — não perca tempo nele. O que se deve ao Jogador é dizer de onde veio a regra que decidiu a conta; a ele só volta o que continuar ambíguo depois da pesquisa, porque aí é ruling de mesa, não lacuna sua.

Três coleções não são escolha e sim regra que a fatia referencia: `propriedades-de-arma`, `propriedades-de-armadura` e `tabelas`. Abra-as quando uma propriedade ou uma tabela de sistema decidir a conta — `mighty` deixa o ataque escolher entre Strength e Dexterity, `powered` fixa a Strength de quem veste a armadura, e o mínimo de atributo para multiclasse só existe lá. Elas não entram em `fontes`: quem as referencia é a fatia do item ou da classe, que já tem linha.

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
- Descoberta operacional durável vira memória em `.agents/memory/`, não comentário em arquivo.
- A harness ainda está sendo construída: o mapa e os tickets vivem em `.scratch/sw5e-harness/`, na raiz do workspace (`/root/projetos`).
