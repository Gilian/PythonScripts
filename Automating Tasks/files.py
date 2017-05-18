import os

file = open(os.getcwd() + '\\text.txt', 'w')
file.write('Geilo!')
file.close()

file = open(os.getcwd() + '\\text.txt')
print(file.read())
