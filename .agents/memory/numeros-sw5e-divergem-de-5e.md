---
name: numeros-sw5e-divergem-de-5e
description: A memória de 5e erra números de SW5e que parecem óbvios — conferir a Fatia mesmo quando a conta parece trivial
metadata:
  type: reference
---

Montar ficha de SW5e "de cabeça" produz números que **parecem** certos e não são.
Casos já pegos em fichas reais:

- **`Combat suit` é `CA 11 + Dex modifier`**, não 12. A intuição vem do studded
  leather de 5e e infla a CA de todo personagem de armadura leve.
- **`Piloting` é perícia de Intelligence**, não de Dexterity.
- **`Tech Points` do Engineer é `nível × 2 + modificador de Intelligence`**, e a
  coluna `Tech Points` da tabela mostra só a primeira parcela. A prosa do
  `classFeatureText` é quem tem a conta.
- **`Duelist Style` não dá o +2 do `Dueling` de 5e**, e `mighty` deixa o arco
  atacar com Strength.

**Por quê:** SW5e reescreve números sem avisar, e o erro é sempre plausível — ele
não salta na leitura da ficha pronta.

**Como aplicar:** a conta que parece trivial demais para abrir a Fatia é
justamente a que erra. Abra a Fatia da armadura antes de somar CA, a da perícia
antes de escolher o atributo, e leia a prosa da classe antes de copiar a coluna
da tabela — a coluna é a fonte, não a resposta.
