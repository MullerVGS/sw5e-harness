---
name: evoluir-personagem
description: Evolui uma ficha já gravada — lê a ficha do repo, grelha o que mudou, aplica o nível contra o Espelho, recalcula os derivados e reescreve preservando a narrativa. Use quando ele disser que subiu de nível, que trocou de equipamento, ou que o personagem mudou na mesa.
---

# evoluir-personagem

**A ficha do repo é a entrada e é a verdade.** Não há export de VTT, planilha nem
print: o que mudou na mesa entra falando, e todo o resto já está gravado.

## Ler antes

O ritual de abertura já te deu a Campanha e o Contexto. Falta:

- **a ficha, inteira** — ela é a entrada;
- a cauda da Crônica, que é onde está o que o personagem viveu desde a última
  vez;
- `FICHA.md`, na hora de escrever.

## A conversa

Ele diz o que mudou, e três coisas mudam sem serem a mesma coisa:

1. **Nível** — a parte mecânica, e ela é sua inteira. Ele diz "subi para 6".
2. **Equipamento** — o que ganhou, perdeu ou trocou. Só ele sabe; nada no
   Espelho adivinha.
3. **O que o personagem virou** — a Crônica te dá o material, ele confirma o que
   ficou.

A única pergunta de regra que vale fazer é onde o nível caiu, e só quando
multiclasse está em jogo: "mais um de Engineer, ou o primeiro de Scout?". É
escolha de conceito disfarçada de regra. O resto — arquétipo, poder, exploit,
ASI ou feat — é seu.

## O acordo

Antes de aplicar, duas linhas: o que o nível traz e o que você vai escolher
dentro dele. Mesma economia da criação — errar aqui custa uma frase, errar
depois custa a ficha. Da Conferência ele não participa.

## O diff é mecânico

A ficha é o rol completo do que o personagem já ganhou; a tabela diz o que o
nível novo dá. A diferença entre as duas é o trabalho inteiro, e ela se lê:

- **A linha do novo nível em `levelChanges`** da classe. É a lista autoritativa
  do que se ganha.
- **Coluna `Features` menos o rol de `features` da ficha** = o que falta ganhar.
  Se sobrar coisa de nível **anterior**, a ficha estava incompleta: é aqui que
  isso aparece, e você conserta agora.
- **Rótulo genérico não nomeia nada.** Cada classe tem o seu — `Discipline
  feature` no Engineer, `Practice feature` no Operative, `Tradition feature` no
  Consular, e assim nas dez. Ele quer dizer "abra o arquétipo".
- **`"�"` é nada neste nível** — não é conteúdo, e o nível ainda dá PV e coluna.
- **Coluna `*Known` que subiu** = quantos poderes a mais se escolhe. A lista
  fica com o tamanho exato da coluna.
- **Toda outra coluna que mudou** vai para `recursos`, com o valor efetivo: a
  Fatia às vezes manda somar um modificador ao que a coluna diz.
- **`Proficiency Bonus` que subiu contamina a ficha inteira** — ataque,
  salvaguarda, DC e bônus de ataque de poder. Recalcule tudo; não conserte só o
  que chamou atenção.

**O texto da regra se acha pelo marcador de nível**, e é o mesmo na classe
(`classFeatureText`) e no arquétipo (`text`): `### <Nome da feature>` seguido de
`_**<Entidade>:** 6th level_`. Procure o marcador do nível novo e você tem a
feature e a prosa dela sem ler a Fatia inteira. Tabela própria de arquétipo
existe, mas é rara — 17 dos 138 —, então no arquétipo o marcador é a regra e a
tabela é a exceção.

**PV do nível novo**: a mesa usa média fixa ou rolagem, e isso é fato dela. Se o
Contexto não disser, pergunte uma vez e grave `- **PV por nível**: <o que ele
disser>` na seção `Mesa`. A entrevista da `nova-campanha` não pergunta porque,
no dia de abrir a mesa, ninguém decidiu ainda — da segunda evolução em diante,
está lá e não se pergunta de novo.

## A narrativa se preserva

`conceito`, `tracos`, `ideais`, `vinculos`, `fraquezas` e `historia` não se
reescrevem porque o personagem subiu de nível. O que o jogo mexe:

- **`ganchos`** é o campo que gira: gancho que a mesa resolveu sai, o que as
  sessões abriram entra.
- **`historia`** ganha no máximo uma frase, e só quando aconteceu algo que
  redefine quem ele é.
- **`aparencia`** muda quando a mesa marcou o corpo — cicatriz, prótese, mão
  perdida.

Reescrever narrativa boa é o jeito mais fácil de estragar uma ficha, e ninguém
percebe até querer relê-la.

## Conferir

O checklist do `FICHA.md` inteiro, de novo — evolução não confere só o delta,
porque o delta contamina. Três erram mais aqui do que na criação:

- **Bônus de proficiência que subiu e ficou pela metade**: um ataque atualizado,
  o outro não.
- **`features` que não cobre todos os níveis.** O item 8 do checklist é o que
  pega feature esquecida lá atrás, e a evolução é quando ela aparece.
- **Recurso copiado da coluna** em vez do valor efetivo, quando a Fatia manda
  somar modificador de atributo.

Estado de mesa continua fora: PV corrente, ponto gasto, crédito e munição não
entram na evolução — e ele vai falar dos quatro enquanto conta o que aconteceu.

Não fechou, não grava.

## Gravar

- **O mesmo arquivo.** Evolução não cria ficha nova e não existe histórico de
  ficha: o que aconteceu está na Crônica, e as versões estão no git.
- **Feature nova entra na ordem de nível**, não no fim da lista. É o que mantém
  barata a comparação com a coluna `Features` na evolução seguinte.
- **A linha do grupo no Contexto carrega o nível** (`<Species Class N>`) —
  atualize. Se o grupo inteiro subiu, `Nível do grupo` também.
- **A Crônica não é tocada.** Subir de nível não é sessão; a sessão foi
  registrada pela `registrar-sessao`.
- **Commit** `ficha: <Nome> <novo nível>`.

## Fechar

Meia dúzia de linhas com o que mudou de fato para a mesa: os números novos e o
que ele passou a poder fazer. Não repita a ficha — ele conhece o personagem.

Se conjura, a lista completa do que ele lança sai de novo aqui, já com o poder
novo dentro, pelo mesmo motivo da criação: na mesa ele quer a lista, não a regra
de composição.
