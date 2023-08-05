days = int(input("Введите количество рассматриваемых дней: "))
degrees = []
thaw = 0
longestThaw = 0

while days > 0:
    degrees.append(int(input()))
    days -= 1

for degree in range(len(degrees)):
    if degrees[degree] > 0:
        thaw += 1
    else:
        longestThaw = max(thaw, longestThaw)
        thaw = 0

if longestThaw < thaw:
            longestThaw = thaw

print("Самая длинная оттепель длилась ", longestThaw, " дней")