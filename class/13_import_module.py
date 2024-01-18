# Wir wollen zufällige Zahlen generieren. Dafür gibt es das Modul random
import random

# Wir können unsere Bibliothek mit as umbenennen.
import random as zufall

zufaellige_zahl = zufall.randint(1, 6)

print(zufaellige_zahl)

# Wir können auch einzelne Funktionen aus einer Bibliothek importieren
from random import randint

print(randint(1, 6))
# print(random)
# print(random.randrange())

# Wir können auch mehrere Funktionen aus einer Bibliothek importieren und
# diese umbenennen

from random import randint as zufallszahl, randrange as zufallsbereich

print(zufallszahl(1, 6), zufallsbereich(1, 6))

# Alles aus dem Modul random importieren

# from random import *

# print(randint(1, 6), randrange(1, 6))

# Lucas empfiehlt diese beiden Schreibweisen:
# import random as zufall
# from random import randint as zufallszahl, randrange as zufallsbereich
