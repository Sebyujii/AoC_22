with open("E:\Code\AoC_22\problems\day_2.txt") as file:
    score = 0
    while line := file.readline():
        if line[2] == "X": # stone on my side
            score += 1
            match line[0]:
                case "A": # stone on other side - draw
                    score += 3
                case "B": # paper on other side - loose
                    score += 0
                case "C": # scissors on other side - win
                    score += 6
        elif line[2] == "Y": # paper on my side:
            score += 2
            match line[0]:
                case "A": # stone on other side - win
                    score += 6
                case "B": # paper on other side - draw
                    score += 3
                case "C": # scissors on other side - loose
                    score += 0
        elif line[2] == "Z": # scissors on my side:
            score += 3
            match line[0]:
                case "A": # stone on other side - loose
                    score += 0
                case "B": # paper on other side - win
                    score += 6
                case "C": # scissors on other side - draw
                    score += 3
    print(score)