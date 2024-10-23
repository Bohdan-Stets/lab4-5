N = int(input("Введіть число N: "))

a, b = 0, 1
while True:
    print(a, end=" ")
    if a != 0 and a % N == 0:
        break
    a, b = b, a + b
