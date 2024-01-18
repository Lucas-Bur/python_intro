# Wir können auch Funktionen von anderen Dateien importieren. Dazu müssen wir die Datei importieren und den Namen der Funktion angeben.
# Dafür benötigen wir eine Datei mit einer Funktion.


def invert_string_case_by_char(string):
    inverted_string = ""
    for character in string:
        if character.islower():
            inverted_string += character.upper()
        else:
            inverted_string += character.lower()
    return inverted_string


def invert_string_case_by_char1(string):
    inverted_string = ""
    for character in string:
        if character.islower():
            inverted_string += character.upper()
        else:
            inverted_string += character.lower()
    return inverted_string
