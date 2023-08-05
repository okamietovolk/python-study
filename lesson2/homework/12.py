numbesSum = int(input())
numbersMul = int(input())
divisors = [1]
flag = True

for divisor in range(1, numbersMul + 1):
    if numbersMul % divisor == 0:
        divisors.append(divisor)

flag = True

for divisor in divisors:
    for divisor2 in divisors:
        if divisor + divisor2 == numbesSum and flag == True:
            result = str(divisor) + " " + str(divisor2)
            flag = False

print(result)