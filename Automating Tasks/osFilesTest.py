import os

# Gets the total size of a folder with all content
'''
totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)
'''

# Read a file
'''
exampleFile = open('C:\\Users\\Tobi\\Documents\\PythonScripts\\test.txt')
fileContent = exampleFile.read()
print(fileContent)
'''
# Read a file with explicit READ permissions
'''
exampleFile = open('C:\\Users\\Tobi\\Documents\\PythonScripts\\test.txt', 'r')
fileContent = exampleFile.read()
print(fileContent)
'''
# Write a file, gets created if it doesent exist
'''
exampleFile = open('C:\\Users\\Tobi\\Documents\\PythonScripts\\test.txt', 'w')
exampleFile.write('Lasst uns etwas neuen Inhalt einfügen um die Datei zu verändern')
exampleFile.close()
exampleFile = open('C:\\Users\\Tobi\\Documents\\PythonScripts\\test.txt')
fileContent = exampleFile.read()
print(fileContent)
'''
# Write a file but append to it's original content
exampleFile = open('C:\\Users\\Tobi\\Documents\\PythonScripts\\test.txt', 'a')
exampleFile.write('Hier noch ein bisschen mehr Text')
exampleFile.close()
exampleFile = open('C:\\Users\\Tobi\\Documents\\PythonScripts\\test.txt', 'r')
fileContent = exampleFile.read()
print(fileContent)
