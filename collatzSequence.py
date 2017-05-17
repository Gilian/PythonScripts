def collatz(number):
    while number != 1:
        if (number % 2) == 0:
            number = number // 2
            print(number)
        else:
            number = 3 * number + 1
            print(number)

print('Hello! Please type in some value.')
try:
    collatz(int(input()))
except ValueError:
    print('Please enter a numerical value')
