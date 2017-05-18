import re
import os

textFile = open(os.getcwd() + '\\countFirstLetter.txt')
inputText = textFile.readlines()

searchValue = '123'

while int(searchValue) < 999:
    searchString = re.compile(str(searchValue))

    counter = 0

    for lines in inputText:
        if not searchString.search(lines) == None:
            mo = searchString.search(lines)
            counter += 1

    if counter > 0:
        print('Matches ' + str(counter) + ", Gesucht nach: " + str(searchValue))
    searchValue = int(searchValue) + 1
