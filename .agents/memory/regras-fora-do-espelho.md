---
name: regras-fora-do-espelho
description: Onde achar as regras de SW5e que a API não serve — custo de casting, o que cada kit faz, feat de 1º nível e as regras de companheiro
metadata:
  type: reference
---

O Espelho cobre **conteúdo** (entidades escolhíveis), não **regra de capítulo**. O
que falta e onde achar, verificado em 2026-07-25:

- **Custo de conjuração**: um poder de nível N custa **N + 1 pontos** de Força ou
  de tech. Poder de nível 1 = **2 pontos**. Poder at-will = grátis. É a
  simplificação do spell point variant do DMG, e não está em Fatia nenhuma.
- **O que cada kit faz**: as Fatias de `Slicer's kit`, `Security kit`,
  `Tinker's implements` e `Astrotech's implements` têm **só custo e peso**. As
  descrições seguem o padrão do Xanathar's — cada kit dá *insight* em perícias
  específicas e tem uma habilidade de calibração (teste DC 15 num descanso, que
  concede um dado de bônus até o bônus de proficiência, ou o dobro com expertise).
- **Feat no 1º nível**: todo personagem ganha um, e mais em 3, 6, 9, 12, 15 e 18.
  Não há Fatia que diga isso; o que o Espelho mostra é o `featOptions` de todo
  background.
- **Regras de companheiro** — o "Customization Options document for Expanded
  Content" que os arquétipos `(Companion)` citam é o
  [Workspace 24 — Companions](https://www.gmbinder.com/share/-MD4vx8qLc1ObQaxb5-X),
  em GMBinder. **Não está na API**, então o sync nunca vai baixá-lo.
- **Não há lista de poderes por classe**: a feature de casting dá acesso à lista
  inteira de Força ou de tech, o que torna o `INDEX.md` de `poderes/` a única
  restrição real na escolha.

**Por quê:** o `sync-espelho.py` rebaixa `https://sw5eapi.azurewebsites.net`, e a
API publica entidades, não capítulos. O site sw5e.com é SPA e não responde a
fetch — as páginas voltam vazias.

**Como aplicar:** conteúdo que vira campo de ficha continua vindo só do Espelho —
nome que não tem Fatia não entra em `fontes`. **Regra** é outra coisa: quando o
Jogador precisar entender como algo funciona, buscar fora é legítimo, e o que se
deve a ele é dizer **de onde veio** — Fatia, esta memória, ou web. Ver
[[droid-companheiro-no-nivel-1]] e [[numeros-sw5e-divergem-de-5e]].
