# Context Map

Mapa dos contextos deste workspace de criação de personagens.

## Contextos

- [Harness](./GLOSSARY.md) — vocabulário da própria ferramenta (papéis, campanha, ficha, espelho, conferência)

### Campanhas

Um contexto por mesa em `campanhas/<slug>/GLOSSARY.md`. A skill `nova-campanha` registra cada uma aqui, na forma:

```
- [Nome da campanha](./campanhas/<slug>/GLOSSARY.md) — papel do Jogador, era, uma linha sobre o tom
```

- [Tauó dos Vitoriosos](./campanhas/tauo-dos-vitoriosos/GLOSSARY.md) — jogador, 25 BBY (Legends), clã mercenário mandaloriano sem trono vivendo de contrato

## Relações

- **Campanha → espelho**: toda ficha consome o Espelho (`sw5e/`), que é comum a todas as campanhas e não pertence a nenhuma. Restrição de fontes permitidas é decisão da mesa e vive no contexto dela, não no Espelho.
- **Estado × histórico**: dentro de uma campanha, `GLOSSARY.md` guarda o que é verdade agora e `CRONICA.md` guarda o que aconteceu. Uma sessão registrada só muda o `GLOSSARY.md` por Promoção.
- **Cânon**: não é um contexto deste repo. Só a Divergência do cânon é registrada, dentro da campanha que diverge.
