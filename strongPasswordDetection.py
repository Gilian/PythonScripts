# Testet eine Eingabe auf Sicherheit als Passwort

import re


def isItSafe(passwort):

    # Mind. 8 Stellen
    passwortRegex_1 = re.compile(r'(.{8,})')

    # Groß und Kleinschreibung
    passwortRegex_2 = re.compile(r'([A-Z]+[a-z]+\w*\d*)|([a-z]+[A-Z]+\w*\d*)')

    # Eine Zahl
    passwortRegex_3 = re.compile(r'(.*\d.*)')

    mo1 = passwortRegex_1.search(passwort)
    mo2 = passwortRegex_2.search(passwort)
    mo3 = passwortRegex_3.search(passwort)

    if mo1 != None and mo2 != None and mo3 != None:
        print("Das Passwort ist sicher")
    else:
        print("Das Passwort ist unsicher")
    # print(mo1.group())
    # print(mo2.group())
    # print(mo3.group())


isItSafe("aberichBinimme2rklein")
