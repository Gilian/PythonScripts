# Sucht die Knightmoves in den Pattern

import re
import os
import pprint

# Liste mit Knightmoves, 16 Möglichkeiten
knightmoves = [18, 16, 27, 29, 34, 38, 43, 49, 61, 67, 72, 76, 81, 83, 92, 94]
# Zählt die Häufigkeit der verschiedenen Knighmoves
knightmoves_count = {18: 0, 16: 0, 27: 0, 29: 0, 34: 0, 38: 0, 43: 0, 49: 0, 61: 0, 67: 0, 72: 0, 76: 0, 81: 0, 83: 0,
                     92: 0, 94: 0}

# Öffnen und lesen des Files
file = open(os.getcwd() + '\\countFirstLetter.txt')
fileContent = file.readlines()
file.close()

# Zähler für Knightmoves insgesamt
counter = 0

# Geht durch die Zeilen im File
for lines in range(len(fileContent)):
    # Geht durch die Suchstrings
    for items in range(len(knightmoves)):
        searchstring = re.compile(str(knightmoves[items]))
        result = searchstring.findall(fileContent[lines])
        if len(result):
            print('Gefunden: ' + str(result) + " in " + str(fileContent[lines]))
            for entries in range(len(result)):
                # Bei mehreren Einträgen pro Zeile müssen alle gezählt werden
                knightmoves_count[int(result[entries])] += 1
            counter += 1

print('Anzahl gefundener Moves: ' + str(counter))
pprint.pprint(knightmoves_count)
