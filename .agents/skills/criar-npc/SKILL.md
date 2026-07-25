---
name: criar-npc
description: Cria um NPC ou inimigo numa Campanha que já existe — grelha curto, monta a ficha a partir de um bloco de monstro do Espelho ou de níveis de classe, confere e grava em campanhas/<slug>/npcs/ ou inimigos/. Use quando ele pedir um NPC, um contato, um capanga, uma tripulação ou um adversário.
---

# criar-npc

Um NPC no meio de outra coisa: ele está preparando sessão, ou acabou de inventar
alguém enquanto conversava, e quer a ficha agora. Grelhar como se fosse PC é o
jeito errado de servir isso.

## Ler antes

O ritual de abertura já te deu a Campanha e o Contexto. Falta:

- a cauda da Crônica, se o NPC já apareceu — é lá que está o que ele já fez;
- as fichas de `npcs/` e `inimigos/`, para não repetir função dentro do elenco.

## A conversa

Curta. A Seed costuma trazer conceito e papel juntos — "um capanga hutt que
cobra dívida do grupo" — e o que falta é quase sempre uma coisa só.

O que só ele sabe:

1. **Para que o NPC serve** — encosta o grupo numa cena, ou volta? É isto que
   decide a pasta e a fidelidade, não o alinhamento.
2. **Quanto ele aguenta**, se briga. Pergunte em cena, não em número: "segura o
   grupo por quanto tempo?" vale mais que "qual CR?".
3. **A ligação com o que está na mesa** — de quem ele é dívida, contato ou
   inimigo. Nomeie as figuras do Contexto ao perguntar.

Nome, aparência e maneirismo você escreve. Se ele já disse o nome, é aquele.

## Bloco ou níveis

Duas formas de montar, e a escolha é sua:

- **De bloco de monstro** (`base` na ficha) — os números já vêm resolvidos e a
  montagem custa uma Fatia. É o certo para quem existe por causa de uma cena.
  Escolha pelo Índice de `monstros/`, que traz CR, CA e PV em cada linha.
- **Com níveis de classe** (`build`, sem `base`) — vira uma ficha comum com
  `"tipo": "npc"`. Custa o mesmo que um PC, e é o certo para quem vai voltar,
  crescer junto com o grupo, ou ser jogado por outra pessoa.

Na dúvida, bloco: promover um bloco a níveis depois é barato; o contrário é
trabalho jogado fora.

## Montar do bloco

O `base` é o recibo. Senses, imunidade, resistência e desafio ficam na Fatia e
**não viram campo** — para a ficha vai o que a mesa usa na cena: atributos, CA,
PV, deslocamento, salvaguardas, perícias e idiomas.

- **O bônus de proficiência não está no bloco.** Ele sai do CR, e a conta é sua.
- **`behaviors` é duas coisas.** O que tem `attackType` vira `ataques`, com o
  bônus e o dano **copiados** — bloco de monstro não é montado pelas regras de
  PC, e refazer a conta pelos atributos dá outro número. O resto vira `features`
  com `origem: "base"` e resumo de uma linha.
- **O bloco nomeia equipamento que não é Fatia** — "heavy combat suit" não
  existe no Espelho. Prevalece o número do bloco; se você nomear um item, ele
  tem que ser Fatia e ganha linha em `fontes`.
- **`languages` vem quebrado** onde a frase tinha "and": o Gamorrean Guard sai
  como `["Gamorrese", "Galactic Basic (underst", "s but can't speak)"]`. Remonte
  a frase, como no `weaponProficiencies` das classes.
- A prosa do bloco às vezes chama a criatura por outro nome — o Gamorrean Guard
  fala em "the berserker". É erro da origem: use o nome do bloco.

Mudar o bloco é permitido, e é o que faz o NPC ser desta mesa e não do livro:
troque a arma, suba um atributo, dê um poder. O que você mudou entra em `notas`,
porque quem reabre a ficha compara com o `base` e precisa saber o que é seu.

## Montar com níveis

Mesma ordem da `criar-personagem`, com duas diferenças. A `narrativa` é enxuta —
conceito e gancho; traço, ideal, vínculo e fraqueza são do PC. E o `nivel` não é
o do grupo por obrigação: um contato veterano é de nível alto e nunca entra em
combate, um capanga é de nível 2.

## Conferir

O checklist do `FICHA.md` inteiro. O que erra mais em NPC:

- **Copiar para a ficha o que o `base` já guarda** — senses, imunidade, CR. A
  ficha incha e passa a mentir quando o Espelho for sincronizado de novo.
- **`base` e `build` juntos.** É um ou outro: ou o bloco é a build, ou há níveis.
- **Narrativa de PC num NPC** — se você escreveu quatro traços de personalidade
  para um capanga, era um PC que você estava montando.

## Gravar

A convenção de gravação é a da `criar-personagem`; muda a pasta:

- **`npcs/`** para aliado, contato e tripulação; **`inimigos/`** para adversário.
  A distinção é de intenção, e intenção muda — quem move o arquivo depois é a
  `registrar-sessao`.
- **O Contexto da campanha só ganha linha se o NPC for recorrente.** Figura que
  a mesa vai continuar encontrando entra em `Facções e figuras`; NPC de uma cena
  não entra, ou o Contexto para de caber numa tela.
- **A Crônica não é tocada.** Criar NPC não é sessão — ele ainda não apareceu.
- **Commit** `ficha: <Nome>`.

## Fechar

Meia dúzia de linhas: quem ele é, e os números que a mesa vai usar quando ele
entrar em cena — CA, PV, iniciativa, os ataques, e a DC se conjurar. Se é
inimigo, uma linha do que ele faz no primeiro turno vale mais que o bloco
inteiro.
