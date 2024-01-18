# Wir wollen die Zahlen kategorisieren und zusätzliches Wissen generieren

zahlen_text = ""
with open("class/input/mock3.txt") as file:
    zahlen_text = file.read()

# print(zahlen_text)

zahlenliste = [int(zeichenkette) for zeichenkette in zahlen_text.split("\n")]
print(zahlenliste)

# welche Zahlen ins < 0, welche sind = 0 und welche sind > 0?

kleiner1 = []
gleich1 = []
groesser1 = []

for zahl in zahlenliste:
    if zahl < 0:
        kleiner1.append(zahl)
    elif zahl == 0:
        gleich1.append(zahl)
    else:
        groesser1.append(zahl)

print(kleiner1, gleich1, groesser1)

kleiner2 = [zahl for zahl in zahlenliste if zahl < 0]
gleich2 = [zahl for zahl in zahlenliste if zahl == 0]
groesser2 = [zahl for zahl in zahlenliste if zahl > 0]

# print(kleiner2, gleich2, groesser2)

# finde die größte zahl aus der kleiner Liste
# finde die kleinste zahl aus der größer Liste

groesste_von_klein = max(kleiner1)
kleinste_von_gross = min(groesser1)

print(kleinste_von_gross, groesste_von_klein)

ausgabe = {
    "klein": {"liste": kleiner1, "groesstes": groesste_von_klein},
    "gleich": gleich1,
    "groesser": {"liste": groesser2, "kleinstes": kleinste_von_gross},
}

print(ausgabe)

import json

with open("class/output/mock20.json", "w") as out_file:
    out_file.write(json.dumps(ausgabe))
