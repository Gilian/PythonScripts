# Gibt die durchschnittliche Länge jeder Zeile an

import os

textFile = open(os.getcwd() + '\\pattern\\all_pattern.txt')
inputText = textFile.readlines()
completeLenght = 0

# Addiere alle Zeilen

for lines in inputText:
    completeLenght += (len(lines)-1)

averageLenght = (completeLenght / len(inputText))

print(averageLenght)

