wmq = int(input())
wms = []

while wmq > 0:
    wms.append(int(input()))
    wmq -= 1

wmMax = wms[0]
wmMin = wms[0]

for wm in wms:
    if wm > wmMax:
        wmMax = wm
    if wm < wmMin:
        wmMin = wm

print(wmMax, wmMin)