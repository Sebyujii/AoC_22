import textwrap

with open("E:\Code\AoC_22\problems\day_3.txt") as file:
    priority=0
    while line := file.readline():
        equal = ''
        # print(f"size: {0.5*(len(line)+1)}")
        parts = textwrap.wrap(line, int(0.5*(len(line)-1)))
        for a in parts[0]:
            for b in parts[1]:
                if a==b:
                    equal = a
                    break
        # print(f"a: {parts[0]}, b: {parts[1]}, zeichen: {equal}")
        if(len(equal) > 0):
            if ord(equal[0]) < 97: # falls Großbuchstabe
                priority += ord(equal) - 38
                print(f"prio+= {ord(equal) - 38}")
            else:
                priority += ord(equal) - 96
                print(f"prio+= {ord(equal) - 96}")
    print(f"Prio: {priority}")
