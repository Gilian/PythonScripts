# This is a guessing game
import random

# Globale variable
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Asking the player for input
for guessesTaken in range (1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # The player guessed correct

if guess == secretNumber:
    print('Very good! You guessed the number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number is was thinking of was ' + str(secretNumber))
    
