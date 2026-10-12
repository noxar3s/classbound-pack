# ClassBound SMP — resource pack

Tekstury itemów klas z pluginu ClassBound SMP. Serwer wysyła paczkę graczom przy wejściu.

Działa tylko na itemy klas: plugin nadaje im komponent `item_model` = `classbound:<klasa>`
(`classes.<id>.item.model` w configu pluginu). Zwykłe łuki, topory itd. zostają vanillowe.

Minecraft **1.21.11** (`pack_format: 75`).

## Struktura

```
pack.mcmeta
assets/classbound/items/<klasa>.json          definicje itemów (od 1.21.4)
assets/classbound/models/item/<klasa>.json    modele (handheld / generated / bow)
assets/classbound/textures/item/<klasa>.png   tekstury 32x32
build.py                                      pakuje ZIP i liczy sha1
```

Klasy z teksturą: archer, wizard, assassin, berserker, illusioner, necromancer, paladin,
stormcaller, vampire. Tank i Pyromaniac nie mają własnej (vanillowa tarcza / fire charge).

## Zmiana tekstury

1. Podmień PNG w `assets/classbound/textures/item/` (przezroczyste tło).
2. `python build.py` — wypisze `sha1`.
3. `git add -A && git commit -m "..." && git push`, potem `git rev-parse HEAD`.
4. W `server.properties` ustaw link przypięty do commita (nie `/main/` — GitHub trzyma go w cache):

```properties
resource-pack=https\://raw.githubusercontent.com/noxar3s/classbound-pack/<HASH>/ClassBound-ResourcePack.zip
resource-pack-sha1=<sha1 z build.py>
require-resource-pack=true
```

Nowa klasa z teksturą: PNG + `items/<id>.json` + `models/item/<id>.json` tutaj i
`model: "classbound:<id>"` w `classes.<id>.item` configu pluginu.
