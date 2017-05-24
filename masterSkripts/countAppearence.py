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
    final_result.append(lines)

# Ausgabe
count = dict(Counter(final_result))
print(count)
x = Counter(count)
x.most_common()
print(x)
