# Context Map

Mapa dos contextos deste workspace de criação de personagens.

## Contextos

- [Harness](./CONTEXT.md) — vocabulário da própria ferramenta (papéis, campanha, ficha, espelho, validação)

### Campanhas

Um contexto por mesa em `campanhas/<slug>/CONTEXT.md`. A skill `nova-campanha` registra cada uma aqui, na forma:

```
- [Nome da campanha](./campanhas/<slug>/CONTEXT.md) — papel do Jogador, era, uma linha sobre o tom
```

_(nenhuma campanha ainda)_

## Relações

- **Campanha → espelho**: toda ficha consome o Espelho (`sw5e/`), que é comum a todas as campanhas e não pertence a nenhuma. Restrição de fontes permitidas é decisão da mesa e vive no contexto dela, não no Espelho.
- **Estado × histórico**: dentro de uma campanha, `CONTEXT.md` guarda o que é verdade agora e `CRONICA.md` guarda o que aconteceu. Uma sessão registrada só muda o `CONTEXT.md` por Promoção.
- **Cânon**: não é um contexto deste repo. Só a Divergência do cânon é registrada, dentro da campanha que diverge.
