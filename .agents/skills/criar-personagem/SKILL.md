---
name: criar-personagem
description: Cria um PC do Jogador numa Campanha que já existe — grelha o conceito, monta a ficha contra o Espelho, confere e grava em campanhas/<slug>/personagens/. Use quando ele pedir um personagem novo, disser que vai entrar numa mesa com alguém, ou abrir com uma Seed de personagem.
---

# criar-personagem

O caminho inteiro da harness: a conversa vira um PC legal e gravado. É sessão de
grilling, não formulário — e o Jogador nunca é perguntado sobre o que ele te
contratou para saber.

## Ler antes

O ritual de abertura já te deu a Campanha e o Contexto dela. Falta:

- a cauda da Crônica, para saber com o que o personagem vai chegar;
- as fichas que já estão em `personagens/`, para não repetir papel dentro do grupo;
- `FICHA.md`, na hora de montar.

O Contexto responde três coisas que por isso **não se pergunta**: nível do grupo,
método de atributos e fontes permitidas. Se o método tira os valores fora da
harness, os valores é que você pede — o método, não.

## A conversa

Uma pergunta por vez, e cada uma tem que caber na cabeça do Jogador sem ele abrir
livro. Classe, arquétipo, perícia e feat são seus.

O que só ele sabe:

1. **O conceito** — quem é essa pessoa, em duas frases. Se ele abriu com uma
   Seed, você já tem isto: devolva o que entendeu e siga.
2. **O que ele faz quando a cena aperta.** É daqui que sai a classe, e é a
   pergunta que ele responde sem saber regra — "atira, some ou conversa?" vale
   mais que "Operative ou Scout?".
3. **A ligação com a mesa** — com quem do grupo ele já tem história, e o que ele
   tem a ver com a Situação. Pergunte nomeando: o Contexto te deu o grupo e as
   figuras, use os nomes.
4. **O rumo** — o que ele quer que aconteça com o personagem. É o que faz
   arquétipo e feat deixarem de ser arbitrários, e é o que vira `ganchos`.
5. **Os atributos**, se a mesa os tira fora. Em point-buy ou array padrão quem
   distribui é você, e aí a pergunta é outra: em que ele é bom e em que é ruim.
6. **Nome e cara**, se ainda não vieram.

Pare aí. Traço, ideal, vínculo, fraqueza e história você escreve do que ele
disse; se faltar matéria para um deles, pergunte por aquele, nunca pela lista.

Uma pergunta a mais é justa quando duas builds legais servem ao conceito e **a
diferença se sente na mesa** — "ele encosta ou cobre de longe?". Nunca quando a
diferença é só de número.

## O acordo

Antes de montar, diga a build em duas linhas — espécie, classe, arquétipo (mesmo
o que só chega mais tarde), background, feat — com meia linha de porquê em cada,
e pergunte se é isso.

É o **único** ponto em que o Jogador decide sobre regra, e é barato: errar aqui
custa uma frase, errar depois custa a ficha. Da Conferência ele não participa —
ela é sua, e não se pede revisão de aritmética a quem chamou você para não fazer
aritmética.

## Montar

Escolha pelo Índice, abra a Fatia, e **escreva a linha de `fontes` no momento em
que abre**. Assim a Legalidade acontece junto com a escolha em vez de virar
auditoria depois, e o que sobrar sem linha no fim é exatamente o nome que você
não conferiu.

Ordem que evita refazer conta: espécie e classe, background, arquétipo,
atributos finais, perícias, poderes, equipamento — e só então derivados, recursos
e ataques, que dependem de tudo acima.

A aritmética é sua. Se ajudar a fechar, escreva um script na hora e jogue fora.

**Regra que o Espelho não tem, você pesquisa.** Toda escolha que a classe
manda fazer tem Fatia, mas a regra que a decide nem sempre: a Fatia manda ver um
capítulo que não foi sincronizado — `Blade Focus` vale para "blade weapons" e
nada na Fatia diz que arma é lâmina. Isso não é buraco para devolver ao Jogador:
a resposta existe, e ir atrás dela é seu trabalho — memória do workspace,
capítulo na API, web, na ordem do custo. Quando a fonte não foi Fatia, `notas`
diz de onde veio. Ao Jogador só volta o que continuar ambíguo depois da Pesquisa
— aí é ruling de mesa, e a decisão é dele. Nome inventado segue pior que dúvida
declarada, porque some na leitura seguinte.

## Conferir

O checklist campo a campo é o do `FICHA.md`; rode-o inteiro antes de gravar. Três
coisas erram com mais frequência em criação do que em qualquer outro momento:

- **Número corrente entrando como máximo** — o Jogador fala em PV que sobrou e
  crédito no bolso enquanto conversa, e nada disso é ficha.
- **Proficiência concedida duas vezes** por espécie, classe, background e feat.
  Antes de trocar a segunda por outra, leia a Fatia dela: com frequência é ela
  que diz no que a repetição vira — o `Loremaster` transforma `Lore` repetida em
  expertise, e quem trocasse de perícia teria jogado a expertise fora.
- **Aumento de atributo esquecido ou contado duas vezes** — o da espécie e o do
  feat entram no valor final, e do valor final não se recupera qual foi qual.

Não fechou, não grava: corrige e confere de novo.

## Gravar

A convenção é esta, e as outras skills de ficha herdam ela em vez de reinventar:

- **Arquivo**: `campanhas/<slug>/personagens/<nome em slug>.json` — `Kael Arvek`
  → `kael-arvek.json`. NPC e inimigo mudam só a pasta.
- **A pasta nasce agora**, com a primeira ficha. Nunca antes, vazia.
- **A linha do grupo no Contexto da campanha passa a valer**: onde estava
  `_ficha a criar_`, entra `<Species Class N>` e a linha de quem ele é. É o
  Contexto ficando verdadeiro, não Promoção — a mesa não jogou nada ainda.
- **A Crônica não é tocada.** Criar personagem não é sessão.
- **Commit** `ficha: <Nome>`.

## Fechar

Não despeje o JSON no chat. Diga em meia dúzia de linhas quem ficou o
personagem, a build fechada, e os números que a mesa vai usar na primeira cena —
PV, CA, iniciativa, os ataques e a DC, se conjurar. Se ficou pendência, ela é a
última linha, não uma nota de rodapé.

Se conjurar, é aqui que a lista de poderes fica **completa**: `poderes` guarda só
os escolhidos, e o que espécie e arquétipo concederam de graça está espalhado
pelas features. Juntar as duas coisas é trabalho de fechamento, não de ficha — na
mesa ele quer uma lista, não uma regra de composição.

Depois: o próximo PC, ou `criar-npc` para o contato que apareceu na conversa.
