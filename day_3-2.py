import textwrap

with open("E:\Code\AoC_22\problems\day_3.txt") as file:
    priority=0
    counter = 1
    while line := file.readline():
        line2 = file.readline()
        line3 = file.readline()
        # print(f"1: {line}, 2: {line2}, 3: {line3}")
        equal = ""
        for a in line:
            for b in line2:
                if a != '\n':
                    if a == b:
                        equal += a
        # print("equal: ", equal)
        for a in equal:
            for b in line3:
                if a != '\n':
                    if a == b:
                        badge = a
                        print("treffer, badge: ", badge)
        if ord(badge[0]) < 97: # falls Großbuchstabe
            priority += ord(badge) - 38
            print(f"badge: {badge}, prio+= {ord(badge) - 38}\n")
        else:
            priority += ord(badge) - 96
            print(f"badge: {badge}, prio+= {ord(badge) - 96}\n")
    print(f"Prio: {priority}")
