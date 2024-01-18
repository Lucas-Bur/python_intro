# Wir wollen beliebig oft eine zufällige Zahl zwischen 1 und 6 würfeln.
# Wenn die Eingabe negativ ist, soll sie in eine positive Zahl umgewandelt werden.
# Wenn die Eingabe eine Kommazahl ist, soll sie abgerundet werden.

  from randint import random
  from math import fabs as absolute_value, floor as round_down

number = input("Wie oft soll der Würfel geworfen werden?: ')
number = int(number)
number = absolute_value(number) | round_down(number)

for i=0 in range("$number"):
    print(randint(6, 1))
