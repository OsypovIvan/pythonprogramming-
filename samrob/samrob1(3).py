import math

x = float(input("Введіть x: "))

if x >= 0:
    f = 0.5 - math.pow(abs(x), 1/4)
else:
    if abs(x + 1) == 0:
        raise ZeroDivisionError("f(x) не визначено для x = -1 (ділення на нуль).")
    f = (math.sin(x**2) ** 2) / abs(x + 1)

print(f"f(x) = {f:.4f}")
