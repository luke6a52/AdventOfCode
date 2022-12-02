with open('2022/Day2.txt', 'r') as input_file:
    lines = input_file.readlines()
rounds = [line.rstrip() for line in lines]

score1 = 0
for round in rounds:
    they, you = round.split()
    if you == 'X':
        score1 += 1
        if they == 'C':
            score1 += 6
        elif they == 'A':
            score1 += 3
    elif you == 'Y':
        score1 += 2
        if they == 'A':
            score1 += 6
        elif they == 'B':
            score1 += 3
    elif you == 'Z':
        score1 += 3
        if they == 'B':
            score1 += 6
        elif they == 'C':
            score1 += 3
print(f'1. Answer is: {score1}')

score2 = 0
for round in rounds:
    they, win = round.split()
    if win == 'X':
        if they == 'A':
            score2 += 3
        elif they == 'B':
            score2 += 1
        elif they == 'C':
            score2 += 2
    elif win == 'Y':
        score2 += 3
        if they == 'A':
            score2 += 1
        elif they == 'B':
            score2 += 2
        elif they == 'C':
            score2 += 3
    elif win == 'Z':
        score2 += 6
        if they == 'A':
            score2 += 2
        elif they == 'B':
            score2 += 3
        elif they == 'C':
            score2 += 1
print(f'2. Answer is: {score2}')