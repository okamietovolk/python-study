n = int(input())
sqr = 2
out = str()
i = 0
while True:
    sqr = 2**i
    i += 1
    if sqr > n:
        break
    out = out + str(sqr) + " "

print(out)
    


