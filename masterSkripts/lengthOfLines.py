# Gibt die durchschnittliche Länge jeder Zeile an

textFile = open('C:\\Users\\Tobi\\Documents\\PythonScripts\\countFirstLetter.txt')
inputText = textFile.readlines()
completeLenght = 0

# Addiere alle Zeilen

for lines in inputText:
    completeLenght += (len(lines)-1)

averageLenght = (completeLenght / len(inputText))

print(averageLenght)

