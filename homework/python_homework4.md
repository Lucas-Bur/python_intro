## Python HA 4

### Aufgabe 1 (20 Punkte)

Öffne die Datei "ha4_aufgabe1_bugs.py" und behebe alle Fehler im Code.

## Aufgabe 2 (30 Punkte)
Schreibe ein Programm, das den Benutzer nach einer Ganzzahl fragt. Es soll die Fakultät (englisch: factorial) der Zahl berechnet und ausgegeben werden. Falls die eingegebene Zahl negativ ist, soll ihr Betrag verwendet werden. (Absolutwert: -7 -> 7)
Nutze die math-Bibliothek für die Berechnung der Fakultät. https://docs.python.org/3/library/math.html

Beispielsausgabe:
```shell
Gib eine Ganzzahl ein: 6
Die Fakultät von 6 lautet: 720

Gib eine Ganzzahl ein: -5
Es wurde eine negative Zahl erkannt. Die Fakultät von 5 lautet: 120
```

### Aufgabe 3 (30 Punkte)
Schreibe ein Programm, was den Inhalt aus der Datei ha4_aufgabe3.txt liest und in eine Liste speichert. Zu jeder positiven Zahl soll 100 addiert werden. Von jeder negativen Zahl soll 100 subtrahiert werden. Die 0 soll unverändert bleiben.
Speichere das Ergebnis in einer neuen Datei ha4_aufgabe3_output.txt.

Beispieleingabe:
```
20
-190
0
```

Beispielausgabe:
```
120
-290
0
```
### Aufgabe 4 (20 Punkte)

1. Lese die Liste von Dictionarys aus der Datei ha4_aufgabe4.json ein.
2. Gehe jeden Eintrag durch und gib die email-Adresse von allen männlichen Personen aus.

## Extra Aufgaben für Extra Punkte

### Extra 1 (30 Punkte)

Schreib eine Programm, was herausfindet, wie oft welches Geschlecht angegeben wurde. Nutze die Datei ha4_extra1.csv als Eingabe.

Beispielsausgabe:
```
Male: 4
Female: 2
Agender: 5
```

### Extra 2 (40 Punkte)

Schreibe ein Programm, dass alle Personen aus der Datei ha4_extra1.csv nach dem angegebenem Geschlecht gruppiert. Zusätzlich sollen nur die Informationen Vorname, Nachname und Email-Adresse ausgegeben werden.
Im Anschluss soll das Dictionary als JSON in einer Datei gespeichert werden.
Nutze gerne die Bibliothek csv und json.

Beispielsausgabe:
```json
{
  "Male": [
    {
      "first_name": "Lefty",
      "last_name": "Callaway",
      "email": "lcallaway2@goo.gl"
    }, {
      "first_name": "Vail",
      "last_name": "Roulston",
      "email": "vroulston9@amazon.de"
    }
  ],
  "Female" : [
    {
      "first_name": "Samantha",
      "last_name": "Dillestone",
      "email": "sdillestonef@indiatimes.com"
    }
  ]
}
```

### Extra 3 (20 Punkte)

Schreibe ein Programm, dass 10000 mal zwei Würfel wirft.
Je Wurf soll in einer Log-Datei die Augenzahl des ersten und zweiten Würfels, sowie dessen Summe gespeichert werden.

Am Ende soll ausgegeben werden, wie oft jede Summe gewürfelt wurde.

Beispielausgabe:
```
2: 278
3: 556
4: 834
5: 1112
6: 1390
7: 1668
8: 1390
9: 1112
10: 834
11: 556
12: 278
```

### Extra 4 (10 Punkte)

Erweitere das Programm, dass der Nutzer zu Beginn die Anzahl der Würfe und die Anzahl der Würfel angeben kann.