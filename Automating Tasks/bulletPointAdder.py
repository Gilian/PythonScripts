#! python3
# bulletPointAdder.py - Adds * to all lines in clipboard

import pyperclip
text = pyperclip.paste()

# Seperate lines and add *
lines = text.split('\n')
print(lines)
for i in range(len(lines)): # loop through the new lines list
    lines[i] = '* ' + lines[i] # add the *

text = '\n'.join(lines)
pyperclip.copy(text)
