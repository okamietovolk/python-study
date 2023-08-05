n = int(input("Введите число: "))

i = 1
fct = 1

while i <= n:
    fct = fct * i
    i += 1

print("Факториал", n, " = ", fct)