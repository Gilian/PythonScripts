import os

# Soll den letzten Charakter einer Zeile zählen

# Öffnen und lesen der Datei
file = open(os.getcwd() + '\\content.txt')
fileContent = file.readlines()
file.close()

counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for lines in fileContent:
    if int(lines[-2]) == 1:
        counter[0] += 1
    elif int(lines[-2]) == 2:
        counter[1] += 1
    elif int(lines[-2]) == 3:
        counter[2] += 1
    elif int(lines[-2]) == 4:
        counter[3] += 1
    elif int(lines[-2]) == 5:
        counter[4] += 1
    elif int(lines[-2]) == 6:
        counter[5] += 1
    elif int(lines[-2]) == 7:
        counter[6] += 1
    elif int(lines[-2]) == 8:
        counter[7] += 1
    elif int(lines[-2]) == 9:
        counter[8] += 1
    else:
        counter[9] += 1


def print_counter():
    for items in range(len(counter)):
        if items < 9:
            print("Anzahl von " + str(items + 1) + " ist gleich: " + str(counter[items]))
        else:
            print("Anzahl von Errors: " + str(counter[items]))


print_counter()
