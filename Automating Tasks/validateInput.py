while True:
    print('Enter your age: ')
    age = input()
    if (age.isdecimal() and (int(age) < 100) and (int(age) > 0)):
        break
    print('Please enter a number for your age. It has to be between 0 and 100')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')
