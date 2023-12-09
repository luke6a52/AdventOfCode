with open('2023/Inputs/Day9.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

sum1 = 0
sum2 = 0
for i, line in enumerate(lines):
    history = [[int(n) for n in line.split(' ')]]
    while any(history[-1]):
        diffs = []
        for k in range(1, len(history[-1])):
            diffs.append(history[-1][k] - history[-1][k-1])
        history.append(diffs)
    for j, diffs in enumerate(history):
        sum1 += diffs[-1]
        sum2 += diffs[0] * (-1)**(j%2)
print(f'1. Answer is: {sum1}') # 1584748274
print(f'2. Answer is: {sum2}') # 1026