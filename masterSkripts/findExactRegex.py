# Find exact string

import re
import os
from collections import Counter

file = open(os.getcwd() + '\\pattern\\imagined_pattern.txt')
inputText = file.read().splitlines()
file.close()

# Speichert die gefunden Muster in einer Tabelle
final_result = []

# Für alle Muster
for lines in inputText:
    # Wenn druch wieder zurücksetzen
    findString = "1234"
    while int(findString) < 99999:
        prog = re.compile('\\b' + lines + '\\b')
        result = prog.findall(str(findString))
        if not result:
            pass
            # print("Empty")
        else:
            print(result)
            final_result += result
        findString = int(findString) + 1

# print(final_result)

count = dict(Counter(final_result))
print(count)