def calc(x, y):
    return x + y


calc = lambda x, y: x ** y
print(calc(2, 5))


def calc(x, y):
    if x > y:
        return x * y
    else:
        return x / y


calc = lambda x, y: x * y if x > y else x / y
print(calc(2, 5))
