with open('2022/Inputs/Day9.txt', 'r') as input_file:
    lines = input_file.readlines()
moves = [line.rstrip() for line in lines]

rope = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
positions1 = {str(rope[1]): 1}
positions2 = {str(rope[9]): 1}
for move in moves:
    dir, count = move.split()
    for i in range(int(count)):
        match(dir):
            case('U'):
                rope[0][1] += 1
                if rope[0][1] - rope[1][1] > 1:
                    rope[1][0] = rope[0][0]
                    rope[1][1] = rope[0][1] - 1
                    positions1[str(rope[1])] = positions1.get(str(rope[1]), 0) + 1
            case('D'):
                rope[0][1] -= 1
                if rope[0][1] - rope[1][1] < -1:
                    rope[1][0] = rope[0][0]
                    rope[1][1] = rope[0][1] + 1
                    positions1[str(rope[1])] = positions1.get(str(rope[1]), 0) + 1
            case('L'):
                rope[0][0] -= 1
                if rope[0][0] - rope[1][0] < -1:
                    rope[1][1] = rope[0][1]
                    rope[1][0] = rope[0][0] + 1
                    positions1[str(rope[1])] = positions1.get(str(rope[1]), 0) + 1
            case('R'):
                rope[0][0] += 1
                if rope[0][0] - rope[1][0] > 1:
                    rope[1][1] = rope[0][1]
                    rope[1][0] = rope[0][0] - 1
                    positions1[str(rope[1])] = positions1.get(str(rope[1]), 0) + 1
                    
print(f'1. Answer is: {len(positions1)}') # 6337   27m 34s
#print(f'2. Answer is: {visible2}') # 157320   58m 22s