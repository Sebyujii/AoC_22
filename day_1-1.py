import os

file = open("E:\Code\AoC_22\problems\day_1.txt", 'r')
top1 = 0
top2 = 0
top3 = 0
# contents = file.read() # buffer gesamten Dateiinhalt in memory - file.line zeigt nur auf erstes zeichen in der line
temp = 0
for line in file:
    if line != "\n":
        temp += int(line)
    else:
        if temp >= top3:
            # print("3")
            if temp >= top2:
                # print("2")
                if temp >= top1:
                    # print("1")
                    top3 = top2
                    top2 = top1
                    top1 = temp
                else:
                    top3 = top2
                    top2 = temp
            else:
                top3 = temp
        temp = 0

print("top1: ", top1)
print("top2: ", top2)
print("top3: ", top3)
print("summe: ", top1+top2+top3)