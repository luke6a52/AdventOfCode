import re

with open('2025/Inputs/Day1.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

dial = 50
sum1 = 0
sum2 = 0
for line in lines:
    num = [int(num) for num in re.findall('\d+', line)][0]
    if line.startswith('L'):
        num = -num
    dial += num
    print(dial)
    if dial%100 == 0:
        sum1 += 1
    if dial >= 100:
        sum2 += dial//100
    elif dial <= 0:
        sum2 += -dial//100 + (num < dial)
    dial = dial%100
print(f'1. Answer is: {sum1}') # 1152
print(f'2. Answer is: {sum2}') # 6671
# time: 00:27:09