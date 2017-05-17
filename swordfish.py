while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue # wieder von vorne
    print('Hello, Joe. What is your password?')
    pwd = input()
    if pwd == 'swordfish':
        break
print('Access granted.')
