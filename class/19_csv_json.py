eintraege = ""

with open("class/input/mock2.csv", "r") as file:
    data = file.read()
    # print(data)

lines = data.split("\n")
# print(lines)

# entfernt und gibt das Element aus
lines.pop(0)
# print(lines)

for i in range(len(lines)):
    lines[i] = lines[i].split(",")

# print(lines)
print("---------------")
# print(lines[3])
print("---------------")
# 3 = Nummer des Eintrags
# 1 ist der Index in dem der Vorname steht
# print(lines[3][1])

import json

data = {}
with open("class/input/mock1.json", "r") as file:
    data = json.load(file)

print(data)
print(data[3]["first_name"])

with open("class/output/mock4.json", "w") as file3:
    file3.write(json.dumps(data))
