n = int(input())
f1 = 0
f2 = 1
f3 = int()
flag = False
i = 1

while f2 <= n or n == f1 and n >= 0 and flag == False:
    if n == f1:
        print("Число ", n, "находится на ", i, "месте в последовательности Фибоначчи")
        flag = True
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    i += 1

if flag == False:
    print("Данное число не является числом Фибоначчи")


    
