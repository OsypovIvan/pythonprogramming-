a = int(input("Введіть перше ціле число: "))
b = int(input("Введіть друге ціле число: "))
c = int(input("Введіть третє ціле число: "))
N = int(input("Введіть N: "))

in_range = [x for x in (a, b, c) if 1 <= x <= N]

if in_range:
    print("Числа з інтервалу [1, N]:", *in_range)
else:
    print("Жодне з чисел не потрапляє в інтервал [1, N].")
