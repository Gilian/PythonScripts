# Liest die Zahl am Anfang jeder Zeile

import os

textFile = open(os.getcwd() + '\\pattern\\all_pattern.txt')
inputText = textFile.readlines()

# Counter mit Zehn stellen, jede Stelle eine Zahl, letzte Stelle Errors
counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Nimmt die Liste und zählt die Zeilen
numLines = len(inputText)

for lines in range(numLines):
    # print('Item ' + str(lines) + ' \n' + inputText[lines])
    firstChar = inputText[lines]
    if int(firstChar[0]) == 1:
        counter[0] += 1
    elif int(firstChar[0]) == 2:
        counter[1] += 1
    elif int(firstChar[0]) == 3:
        counter[2] += 1
    elif int(firstChar[0]) == 4:
        counter[3] += 1
    elif int(firstChar[0]) == 5:
        counter[4] += 1
    elif int(firstChar[0]) == 6:
        counter[5] += 1
    elif int(firstChar[0]) == 7:
        counter[6] += 1
    elif int(firstChar[0]) == 8:
        counter[7] += 1
    elif int(firstChar[0]) == 9:
        counter[8] += 1
    else:
        counter[9] += 1
textFile.close()


def printOutput():
    print("Startknoten und Anzahl: ")
    for lines in range(10):
        if lines < 9:
            print(str(lines + 1) + '  = ' + str(counter[lines]))
        else:
            print("Errors: " + str(counter[lines]))


# print(sorted(counter, reverse=True))

printOutput()
