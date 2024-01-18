dictionary = {"schluessel1": "Hund", "schluessel2": "Katze"}
# liste = ["Hund", "Katze", "Maus"]
# list_dict = {0: "Hund", 2: "Maus", 1: "Katze"}

print(dictionary["schluessel2"])
# print(liste[2])
# print(list_dict[2])

dictionary["schluessel2"] = "Maus"
print(dictionary["schluessel2"], ".....")
dictionary["schluessel3"] = "Mensch"
print(dictionary)

print(list(dictionary.keys()))
print(list(dictionary.values()))

# Wir gehen nacheinander alle Schlüssel durch
for key in dictionary:
    print(key)

schluessel1_in_dict = "schluessel1" in dictionary

print(schluessel1_in_dict)
print("schluessel4" in dictionary)
