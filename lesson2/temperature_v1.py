days = int(input("Введите количество рассматриваемых дней: "))
i = 0
temp = 0
thaw = 0
longestThaw = 0

while i < days:
    t1 = int(input())
    if t1 > 0:
        thaw += 1

    elif t1 < 0:
        if longestThaw < thaw:
            longestThaw = thaw
            thaw = 0
    i += 1
if longestThaw < thaw:
            longestThaw = thaw

print("Самая длинная оттепель длилась ", longestThaw, " дней")
