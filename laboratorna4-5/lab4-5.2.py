N = int(input("Введіть число N (2 ≤ N < 99): "))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if j % 2 == 1:
            print(f"{i}{j}0", end=" ")
        else:
            print("0", end=" ")
    print()

