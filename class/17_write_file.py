# Eine Datei schreiben

# w gibt an, dass wir eine neue Datei erstellen und ggfs. die alte
# Datei überschreiben
# equivalten >
# echo "Hello" > datei.txt

with open("class/output/out0.txt", "w") as file1:
    file1.write("Hello Kurs 23-11")

# x gibt an, dass wir nur eine Datei erstellen, wenn sie nicht
# exisitiert. Falls vorhanden wird Fehler ausgegeben

# with open("class/output/out1.txt", "x") as file2:
#     file2.write("Hallo, ich bin ganz neu hier. :)")

# a gibt an, dass wir eine neue Datei erstellen und ggfs. an die alte
# Datei etwas anhängen
# equivalten >>
# echo "Hello" >> datei.txt

with open("class/output/out2.txt", "a") as file3:
    file3.write("Hello Kurs 23-11\n")
