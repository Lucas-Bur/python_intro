# Wir möchten den Inhalt einer Datei in eine Variable laden.

file1 = open("class/input/mock0.txt")
content1 = file1.read()
file1.close()
# print(content1)

file2 = open("C:\\Users\\lucas\\Documents\\python_intro\\class\\input\\mock0.txt")
content2 = file2.read()
file2.close()
# print(content2)

# with kümmert sich um das Schließen der Datei im Nachgang

with open("class/input/mock0.txt") as file3:
    content3 = file3.read()
    print(content3)

# Good to Know: wenn ihr aus Sicht der Datei arbeiten wollt, hilft
# euch der unten stehende Code

import os

script_path = os.path.dirname(__file__)
relative_path = "input/mock0.txt"
absolute_path = os.path.join(script_path, relative_path)

# print(script_path)
# print(relative_path)
# print(absolute_path)

with open(absolute_path, "r") as file4:
    content4 = file4.read()
    print(content4)
