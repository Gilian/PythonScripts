def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Can not divide by zero.')

print(spam(2))
print(spam(0))
