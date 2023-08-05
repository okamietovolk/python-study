n = int(input())
upCoins = 0
downCoins = 0
coins = []

while n > 0:
    coins.append(int(input()))
    n -= 1

for coin in coins:
    if coin == 1:
        upCoins += 1
    elif coin == 0:
        downCoins += 1

if upCoins < downCoins:
    print(upCoins)
else:
    print(downCoins)