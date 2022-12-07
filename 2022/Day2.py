with open('2022/Inputs/Day2.txt', 'r') as input_file:
    lines = input_file.readlines()
rounds = [line.rstrip() for line in lines]

score1 = 0
loss1 = 0
stats1 = [0,0,0]
for round in rounds:
    match round:
        case 'A X': score1 += 4; loss1 += 4; stats1[1] += 1
        case 'B X': score1 += 1; loss1 += 8; stats1[2] += 1
        case 'C X': score1 += 7; loss1 += 3; stats1[0] += 1
        case 'A Y': score1 += 8; loss1 += 1; stats1[0] += 1
        case 'B Y': score1 += 5; loss1 += 5; stats1[1] += 1
        case 'C Y': score1 += 2; loss1 += 9; stats1[2] += 1
        case 'A Z': score1 += 3; loss1 += 7; stats1[2] += 1
        case 'B Z': score1 += 9; loss1 += 2; stats1[0] += 1
        case 'C Z': score1 += 6; loss1 += 6; stats1[1] += 1
print(f'1. Opponent is  : {loss1}')  # 11536
print(f'1. Answer is    : {score1}') # 15523
print(f'1. Win-Draw-Loss: {stats1}') # [990, 1096, 414]

score2 = 0
loss2 = 0
stats2 = [0,0,0]
for round in rounds:
    match round:
        case 'A X': score2 += 3; loss2 += 7; stats2[2] += 1
        case 'B X': score2 += 1; loss2 += 8; stats2[2] += 1
        case 'C X': score2 += 2; loss2 += 9; stats2[2] += 1
        case 'A Y': score2 += 4; loss2 += 4; stats2[1] += 1
        case 'B Y': score2 += 5; loss2 += 5; stats2[1] += 1
        case 'C Y': score2 += 6; loss2 += 6; stats2[1] += 1
        case 'A Z': score2 += 8; loss2 += 1; stats2[0] += 1
        case 'B Z': score2 += 9; loss2 += 2; stats2[0] += 1
        case 'C Z': score2 += 7; loss2 += 3; stats2[0] += 1
print(f'2. Opponent is  : {loss2}')  # 9379
print(f'2. Answer is    : {score2}') # 15702
print(f'2. Win-Draw-Loss: {stats2}') # [1655, 485, 360]   12m 6s