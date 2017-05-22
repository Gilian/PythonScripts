import re
import os

textFile = open(os.getcwd() + '\\pattern\\imagined_pattern.txt')
inputText = textFile.readlines()

searchValue = '1234567'

while int(searchValue) < 9999999:
    searchString = re.compile(str(searchValue))

    counter = 0

    for lines in inputText:
        if not searchString.search(lines) == None:
            mo = searchString.search(lines)
            counter += 1

    if counter > 0:
        print('Matches ' + str(counter) + ", Gesucht nach: " + str(searchValue))
    searchValue = int(searchValue) + 1
