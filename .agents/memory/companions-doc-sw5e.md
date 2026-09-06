---
name: companions-doc-sw5e
description: O que o documento de Companions do SW5e (GMBinder) diz — Follower, naturezas, droid de classe I–V, tracker droid como alternativa com OK do mestre, o custo dos traits em tech points — e como baixá-lo inteiro com curl
metadata:
  type: reference
---

O "Customization Options document for Expanded Content — Companions" que os
arquétipos `(Companion)` citam é o **Workspace 24 — Companions**, em
https://www.gmbinder.com/share/-MD4vx8qLc1ObQaxb5-X. Lido inteiro em
2026-09-05, para o Astrotech do Kael Arvek.

**Como baixar**: `curl -sL -A "Mozilla/5.0" <url>` devolve o HTML completo
(~490 KB); tirar tags com regex dá ~95 KB de texto limpo, o suficiente para
grepar seções. O WebFetch resume demais e perde tabela — use curl e filtre com
script descartável.

**Estrutura**:

- **Follower** é a classe de todo companion, nível igual ao do dono, proficiência
  de PC. Tabela: 1º dois traits; 2º `Helpful` (Help como ação bônus, só para o
  dono); 3º `Companion Class`; 4º ASI; 5º terceiro trait; 6º Expertise; 7º
  feature de classe; 9º quarto trait; 10º `Companion Freedom` (age sem ação
  bônus do dono) e feat. Sem ação bônus do dono, o companion só faz Dash, Dodge,
  Disengage, Guard ou Hide. Iniciativa: os dois rolam e agem na **menor**.
- **Companion Classes** (3º nível): Berserker, Consular, Engineer, Fighter,
  Guardian, Monk, Operative, Scholar, Scout, Sentinel. Droid é Force Insensitive,
  então só Engineer, Operative, Scholar, Scout e os marciais. O **Engineer de
  companion** não tem tech points: dois poderes de até 1º nível, conjura o de 1º
  uma vez por descanso curto ou longo, e Potent Aptitude próprio (Int mod
  usos). Operative dá Sneak Attack 1d6 e Cunning Action.
- **Naturezas** com pré-requisito: Beast (Animal Handling), Droid (proficiência
  em astrotech's implements), Tracker Droid (conjurar tech), Turret
  (artillerist's implements), Vehicle (mechanic's kit). Humanoid, Spirit e
  Thrall são WIP.
- **Droid Companion**: array 16/14/14/12/10/8, CA 10 + Dex, sem armadura vestida
  (só integrada por quem tem astrotech's), resistência necrotic/poison/psychic,
  vulnerável a ion. Classe I (d8, Medium, 25 pés, uma perícia mental), II (d6,
  **Small**, 25 pés, uma perícia e um specialist's kit, Undersized), III (d8,
  todos os idiomas), IV (d8, 30 pés, armadura leve), V (d8, 30 pés, Athletics e
  artisan's implements). Só voa com `Repulsor Coil`, 9º nível e Classe II.
- **Tracker Droid Companion**: array 16/14/12/10/8/6, d4, **Tiny**, 20 pés, CA
  10 + Dex sem armadura nunca, shockprod finesse de 1 lightning, duas perícias e
  uma ferramenta integrada, alvo válido do TDI. Traits que decidem build:
  `Aerial Travel Package` (voo 30), `Camouflage Module` (invisível, 2 h de
  orçamento), `Techcasting Range Protocol` (o dono conjura através dele),
  `Ranged Interface Protocol` (+50 pés de link), `Sentry Dish` (alarm), os
  `Interfaced * Protocol` só no 5º.
- **Alternative Companions**: o próprio documento diz que "an astrotech engineer
  might prefer to have a tracker droid" e manda combinar com o mestre. É ruling,
  não regra — declare ao Jogador.

**A conta que o arquétipo esconde**: o `Astrotech Engineering (Companion)` dá
dois traits a mais, e "for each droid trait in excess of your proficiency bonus,
your tech point maximum is reduced by 1". No 3º nível são 4 traits contra
proficiência 2: **−2 Tech Points** enquanto os quatro estiverem instalados. A
coluna `Modification Slots` do Engineer, nessa variante, é o número de vezes por
descanso longo que o droid conjura um poder de 1º nível do dono.

**Como aplicar**: companion vira ficha `tipo: npc` em `npcs/`, com `build`
(`Follower` + Companion Class como arquétipo), sem `base`, e `notas` dizendo que
Follower, natureza e classe de companion são seções do documento, não Fatias —
é a única exceção aceita à regra do nome em inglês, porque a Fatia do arquétipo
é quem manda para lá. Ver [[droid-companheiro-no-nivel-1]] e
[[regras-fora-do-espelho]].
