import os


class Muster:
    """Generelle Klasse für jedes Muster"""

    # Instanzvariablen
    muster_zaehler = 0

    def __init__(self, struktur):
        self.struktur = struktur
        Muster.muster_zaehler += 1

    def print_info(self):
        return self.struktur

file = open(os.getcwd() + '\\example_pattern.txt')
file_content = file.readlines()
file.close()

for lines in file_content:
    m1 = Muster(lines)

print(m1.print_info())
