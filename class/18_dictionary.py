# Ein Dictionary ist eine Sammlung von Schlüssel-Wert-Paaren.
# Wir erstellen ein Dictionary mit geschweiften Klammern.

dictionary = {"schluessel1": "Hund", "schluessel2": "Katze"}
# liste = ["Hund", "Katze", "Maus"]
# list_dict = {0: "Hund", 2: "Maus", 1: "Katze"}

# Wir können auf die Werte eines Dictionarys zugreifen, indem wir den Schlüssel in eckige Klammern setzen.

print(dictionary["schluessel2"])
# print(liste[2])
# print(list_dict[2])

# Wir können die Werte eines Dictionarys auch überschreiben, indem wir den Schlüssel in eckige Klammern setzen.

dictionary["schluessel2"] = "Maus"
print(dictionary["schluessel2"])

# Wir können auch neue Schlüssel-Wert-Paare hinzufügen, indem wir den Schlüssel in eckige Klammern setzen.

dictionary["schluessel3"] = "Mensch"
print(dictionary)

# Wir können uns alle Schlüssel und Werte mit keys() und values() asugeben lassen

print(list(dictionary.keys()))
print(list(dictionary.values()))

# Wir gehen nacheinander alle Schlüssel durch
for key in dictionary:
    print(key)

# Mit dem Schüsselwort in können wir überprüfen, ob ein Schlüssel vorhanden ist

schluessel1_in_dict = "schluessel1" in dictionary

print(schluessel1_in_dict)
print("schluessel4" in dictionary)
