with open('2022/Inputs/Day10.txt', 'r') as input_file:
    cmds = [line.rstrip() for line in input_file]

adds = []
for cmd in cmds:
    adds.append(0)
    if(cmd[0:4] == 'addx'):
        adds.append(int(cmd[5:]))
        
x = 1
signals = []
pixels = []
for i, add in enumerate(adds):
    if(i%40 == 19):
        signals.append((i+1)*x)
    if(x - i%40 in [-1,0,1]):
        pixels.append('#')
    else:
        pixels.append(' ')
    x += add

print(f'1. Answer is: {sum(signals)}') # 13060   17m 27s
print('2. Answer is:')
for j in range(6):
    print(''.join(pixels[j*40:(j+1)*40])) # FJUBULRZ   29m 54s