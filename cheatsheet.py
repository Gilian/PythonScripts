# This is a comment
"""
Mathematische Operationen klassisch mit +, -, *, /
2 + 2 = 4
2 / 1 = 2.0
3 % 2 = 1, Rest (modulo)
3 // 2 = 1, Abrunden (floor)
3 ** 2 = 9, Hoch (squared)

Concatination
2.0 + 2 = 4.0
'2' + '2' = '22'
'2' * 3 = '222'
'2' + 2 = Error

Slicing
word = 'python'
word[:] --> python
word[0] --> p
word[-1] --> n
word[:2] --> py
word[2:] --> thon

Sonderzeichen darstellen mit backslash
Oder als raw-String mit r'C:(Backslash)User'

Funktionen
len() --> Länge von Listen, Strings etc.

Komplexe Datentypen
list[1,2,3], Listen sind schneidbar und muteable
"""

# If-Example
if 1 > 2:
    pass
elif 1 < 2:
    pass
else:
    pass

# For-Example
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# For-Example: Kopie machen
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)

# For-Example: Mit Zähler
for i in range(5):
    print(i)

# For-Example: Zähler mit Ausgabe
for w in range(len(words)):
    print(words[w])

# For-Example: Mit Else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


# Weitere Keywords sind: break, continue und pass

# Functions
def test_function(arg):
    """ 
    Beschreibt die Funktion
    :param arg: Beschreibt den param
    :return: kein return hat den Typ None!
    """
    print(arg)


test_function("Ausgabe")


# Functions mit default-Values, VORSICHT: Bei aufeinanderfolgenden Aufrufen, der default wird gespeichert
def default_values(output=4):
    print(output)


default_values()  # Hier wird der default-Wert eingetragen


# Funktion mit keyword
def keyword_value(state="stiff"):
    if state == "stiff":
        print("Default")
    else:
        print("Stiffness: " + str(state))


keyword_value()  # Ausgabe mit keyword

