import sys
import pyperclip

name = input()
print(name)

name = sys.stdin.readline()
print(name)

pyperclip.copy(name)