import math

t = float(input("Введіть t: "))
x = float(input("Введіть x (остання цифра у списку групи): "))

Z = ((9 * math.pi * t + 10 * math.cos(x)) / (math.sqrt(t) - abs(math.sin(t)))) * math.exp(x)

print(f"Результат: {Z:.2f}")
