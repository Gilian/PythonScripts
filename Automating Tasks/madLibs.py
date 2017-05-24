# !python3
# madLibs.py - Replaces the words NOUN, VERB and ADJECTIV in an text
#            - You have the opportunity to save your file

import os

file = open(os.getcwd() + '\\madLibs.txt')
filecontent = file.read()
file.close()


def replace_string(searchstring, content):
    """ 
    Sucht nach einem String und gibt die Möglichkeit ihn durch eine Eingabe zu ersetzen
    Args: 
        searchstring (str): Der String nachdem gesucht wird
        content (str): Der Inhalt der durchsucht wird
    Returns:
        Gibt den veränderten Inhalt zurück
    """
    while content.find(searchstring) is not -1:
        print("Bitte ein", searchstring, "wählen")
        replacement = input()
        content = content.replace(searchstring, replacement, 1)
    return content


# AUFRUFE
filecontent = replace_string("ADJECTIVE", filecontent)
filecontent = replace_string("NOUN", filecontent)
filecontent = replace_string("VERB", filecontent)

# ABLAUF
print(filecontent)
print("Möchten Sie den Inhalt in einer neuen Datei speichern? Y/N")
save_file = input()

if save_file == "Y":
    file = open(os.getcwd() + '\\madLibsOutput.txt', 'w')
    file.write(filecontent)
    file.close()
elif save_file == "N":
    print("Nicht gepspeichert")
else:
    print("Abbruch. Eingabe nicht erkannt!")
