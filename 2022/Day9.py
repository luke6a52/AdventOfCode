with open('2022/Inputs/Day9.txt', 'r') as input_file:
    lines = input_file.readlines()
moves = [line.rstrip() for line in lines]

rope = []
positions = []
for j in range(10):
    rope.append([0,0])
    positions.append({str(rope[j]): 1})
for move in moves:
    dir, count = move.split()
    for i in range(int(count)):
        match(dir):
            case('U'): rope[0][1] += 1
            case('D'): rope[0][1] -= 1
            case('L'): rope[0][0] -= 1
            case('R'): rope[0][0] += 1
        positions[0][str(rope[0])] = positions[0].get(str(rope[0]), 0) + 1
        
        for j in range(1, len(rope)):
            up_down = rope[j-1][1] - rope[j][1]
            left_right = rope[j-1][0] - rope[j][0]
            moved = False
            if up_down      >  1: rope[j][1] += 1; up_down    = 0; moved = True
            elif up_down    < -1: rope[j][1] -= 1; up_down    = 0; moved = True
            if left_right   < -1: rope[j][0] -= 1; left_right = 0; moved = True
            elif left_right >  1: rope[j][0] += 1; left_right = 0; moved = True
            if(moved):
                if up_down      > 0: rope[j][1] += 1
                elif up_down    < 0: rope[j][1] -= 1
                if left_right   < 0: rope[j][0] -= 1
                elif left_right > 0: rope[j][0] += 1
                positions[j][str(rope[j])] = positions[j].get(str(rope[j]), 0) + 1
            
print(positions[1])
print(f'1. Answer is: {len(positions[1])}') # 6337   27m 34s
print(f'2. Answer is: {len(positions[9])}') # 2455   1h 17m