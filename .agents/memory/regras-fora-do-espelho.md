---
name: regras-fora-do-espelho
description: Onde achar as regras de SW5e que o Espelho não guarda — custo de casting, o que cada kit faz, feat de 1º nível e as regras de companheiro
metadata:
  type: reference
---

O Espelho cobre **conteúdo** (entidades escolhíveis), não **regra de capítulo**. O
que falta e onde achar, verificado em 2026-07-25:

- **Custo de conjuração**: um poder de nível N custa **N + 1 pontos** de Força ou
  de tech. Poder de nível 1 = **2 pontos**. Poder at-will = grátis. É a
  simplificação do spell point variant do DMG, e não está em Fatia nenhuma.
- **O que cada kit faz**: as Fatias das ferramentas têm **só custo e peso** — a
  descrição de escopo está no **PHB cap. 5** (`/api/playerHandbookRule`, `rowKey`
  `"5"`). Cada _artisan's implements_ ganha uma linha de ofício explícita, e é ela
  que decide **quem conserta o quê**:
  - **Armstech's implements** → cria e **repara blasters e vibroweapons** (é a
    ferramenta de consertar arma pessoal — inclui slug pistol, que é `SimpleBlaster`).
  - **Armormech's implements** → cria e repara armaduras e escudos.
  - **Artificer's implements** → cria lightweapons. **Astrotech's** → cria e
    modifica droids. **Cybertech's** → wristpads. **Biotech's** → augmentações
    cibernéticas. **Gadgeteer's** → jet packs, friction-grip e afins.
  - **Mechanic's kit** → cria e repara **veículos e naves**, não arma de mão.
  - **Tinker's implements** → "general use", cria pequenos trinkets — a esticada
    plausível quando falta a ferramenta dedicada.
  - Specialist's kits (Slicer's, Security, Forgery, Poisoner's, Disguise, etc.)
    são de propósito, não de ofício: Slicer's fura defesa/trava computadorizada,
    Security fura trava física, e assim por diante.
  O padrão Xanathar's (insight + calibração DC 15) pode existir por cima em
  variante, mas a linha de ofício do PHB é a regra que resolve reparo na mesa.
- **Feat só no 1º nível e trocando ASI**: PHB cap. 4 (`rowKey "4"`, "Background
  Feat") diz que todo background dá um feat inicial, e cap. 6 diz que fora disso
  feat só entra no lugar de um Ability Score Improvement, como regra opcional.
  **Não há feat em 3, 6, 9** — esta memória dizia isso e estava errada;
  corrigido em 2026-09-05. O que o Espelho mostra é o `featOptions` de todo
  background.
- **Regras de companheiro** — o "Customization Options document for Expanded
  Content" que os arquétipos `(Companion)` citam é o
  [Workspace 24 — Companions](https://www.gmbinder.com/share/-MD4vx8qLc1ObQaxb5-X),
  em GMBinder. **Não está na API**, então o sync nunca vai baixá-lo. O que ele
  diz e como baixá-lo está em [[companions-doc-sw5e]].
- **Tipos de dano, e o que ion faz**: PHB cap. 9 (`rowKey "9"`), seção de tipos
  de dano. **Ion** é descrito como "most effective against droids and constructs"
  e desabilita eletrônica simples até ela ser reiniciada — mas **não há redução
  de dano contra criatura orgânica**: 2d4 de `shocking ray` entram inteiros num
  bicho. O que existe do outro lado é a **vulnerabilidade a ion dos droids**, que
  dobra o dano — e vale contra o companion tanto quanto contra o inimigo. EMP na
  ficção da mesa é dano ion na linguagem do sistema. Verificado em 2026-09-20.
- **Não há lista de poderes por classe**: a feature de casting dá acesso à lista
  inteira de Força ou de tech, o que torna o `INDEX.md` de `poderes/` a única
  restrição real na escolha.

**Por quê:** o `sync-espelho.py` rebaixa as entidades escolhíveis de
`https://sw5eapi.azurewebsites.net`. Os dois livros **estão** na API —
`/api/playerHandbookRule` (16 capítulos) e `/api/wretchedHivesRule` (10) — e
ficaram fora do Espelho de propósito (issue 13): regra se pesquisa na hora,
baixando a coleção e filtrando o capítulo com script descartável. O documento de
Companions não tem endpoint; é o link de GMBinder acima. O site sw5e.com é SPA e
não responde a fetch — as páginas voltam vazias.

**Como aplicar:** conteúdo que vira campo de ficha continua vindo só do Espelho —
nome que não tem Fatia não entra em `fontes`. **Regra** é outra coisa: pesquisá-la
é obrigação do Agente — esta memória, o capítulo na API, a web, na ordem do
custo — e o que se deve ao Jogador é dizer **de onde veio**, nunca a dúvida
crua. Ver [[droid-companheiro-no-nivel-1]] e [[numeros-sw5e-divergem-de-5e]].
