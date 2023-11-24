with open("E:\Code\AoC_22\problems\day_2.txt") as file:
    score = 0
    while line := file.readline():
        if line[0] == "A": # rock on other side
            match line[2]:
                case "X": # need to loose - scissors
                    score += 3
                case "Y": # need to draw - rock
                    score += 3 + 1
                case "Z": # need to win - paper
                    score += 6 + 2
        elif line[0] == "B": # paper on other side
            match line[2]:
                case "X": # need to loose - rock
                    score += 1
                case "Y": # need to draw - paper
                    score += 3 + 2
                case "Z": # need to win - scissors
                    score += 6 + 3
        elif line[0] == "C": # scissors on other side
            match line[2]:
                case "X": # need to loose - paper
                    score += 2
                case "Y": # need to draw - scissors
                    score += 3 + 3
                case "Z": # need to win - stone
                    score += 6 + 1
    print(score)