---
name: registrar-sessao
description: Registra uma sessão jogada — escreve a entrada na CRONICA.md da Campanha e promove ao CONTEXT.md só o que virou estado permanente. Use quando ele disser que jogou, pedir para registrar a sessão, ou simplesmente começar a contar o que aconteceu na mesa.
---

# registrar-sessao

A sessão acabou e ele está contando. O trabalho é virar o relato numa entrada
que se explique sozinha daqui a seis meses — e decidir, com disciplina, o que
dela vira estado da mesa.

## Ler antes

O ritual de abertura já te deu a Campanha e o Contexto. Falta a cauda da
Crônica: as duas últimas entradas dizem onde a mesa parou e qual é o próximo
`S<NN>`.

Se ele nomear um NPC que tem ficha, abra a ficha antes de escrever — ela pode
precisar mudar.

## A conversa

Ele conta; você não entrevista. Pergunte só o que falta para a entrada se
explicar sozinha:

- **quando** foi, se não foi hoje;
- **onde** aconteceu;
- **quem estava** — jogador que faltou muda o que dá para concluir da entrada
  depois.

Se o relato vier picado, puxe por ordem ("e aí?"), nunca por seção. Ninguém
lembra da sessão em tópicos.

## A Promoção é a decisão

Escrever a entrada é transcrição. Promover é decisão — e é a única coisa que
você mostra antes de gravar, porque Contexto errado envenena toda ficha lida
depois e ele é quem sabe se aquilo ficou.

Diga em uma linha o que sobe e o que fica só na Crônica, e siga com o que ele
confirmar. O que a forma do arquivo já ensina:

- **A Situação quase sempre muda** — é a seção que existe para isso.
- **Facção e figura mudam pouco, e só por postura.** O cartel virou hostil, o
  contato virou figura recorrente. Que o grupo falou com alguém não é postura.
- **Casa-regra fixada pelo mestre sobe sempre** — é regra, não acontecimento.
- **O grupo muda quando alguém morre, entra ou sai.** Nível não sobe aqui: quem
  mexe em nível é a `evoluir-personagem`.

Na dúvida, não promove — e diga em uma linha o que você deixou de fora, para ele
te contradizer se quiser.

## Escrever

O formato está fixado no cabeçalho da própria `CRONICA.md`; siga-o. Três coisas
fazem a entrada valer daqui a meses:

- **Nomeie quem apareceu com o nome que a ficha usa** — é assim que a busca casa
  depois.
- **3 a 8 linhas.** O que não couber é detalhe de cena, e detalhe de cena não é
  o que se relê.
- **`Promovido` fecha o ciclo**: quem lê a entrada sabe se o Contexto já
  absorveu aquilo. `nada` é resposta boa e frequente.

## O que mais a sessão mexe

- **Ficha de NPC.** Mudou de situação, a ficha muda: gancho que a mesa resolveu
  sai, gancho novo entra. NPC que trocou de lado **muda de pasta** (`npcs/` ↔
  `inimigos/`) — a pasta é intenção, e a intenção mudou.
- **NPC que morreu não é apagado.** A Crônica continua nomeando ele, e a ficha é
  onde se descobre quem era. A morte entra em `notas`, com a sessão.
- **PC que subiu de nível.** A entrada registra que subiu; a ficha é trabalho da
  `evoluir-personagem`, e você diz isso ao fechar.

## Gravar

- **A Crônica é append-only.** Entrada nova no fim, e não se reescreve entrada
  antiga — nem para consertar o que a sessão seguinte desmentiu. O que a mesa
  descobriu depois é conteúdo da entrada de depois.
- **O Contexto absorve a Promoção e continua cabendo numa tela.** Promover é com
  frequência **substituir** uma linha, não acrescentar: o fato que a Promoção
  tornou falso sai junto.
- **Commit** `sessao: <Nome da campanha> S<NN>`.

## Fechar

Duas linhas: o que subiu para o Contexto e o que ficou só na Crônica. Se um PC
subiu de nível, a última linha é o convite para a `evoluir-personagem`.
