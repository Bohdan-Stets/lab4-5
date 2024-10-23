import math

def func(x):
    if x == 0 or x + 3 < 0:
        return None
    return 1/x + math.sqrt(x + 3) + 6

a = float(input("Введіть початок відрізка a: "))
b = float(input("Введіть кінець відрізка b: "))
h = float(input("Введіть крок h: "))

x = a
while x <= b:
    result = func(x)
    if result is None:
        print(f"Недопустиме значення для x = {x}")
    else:
        print(f"x = {x}, y = {result}")
    x += h
