def g(a, b):
    return (a**2 + b**2) / (a**2 + b**2 + 4)

N = int(input("Введіть кількість членів послідовності N: "))
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))

sum_g = 0
for i in range(N):
    sum_g += g(a, b)

print(f"Сума перших {N} членів послідовності: {sum_g}")
