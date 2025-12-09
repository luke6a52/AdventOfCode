import re
import math

with open('2025/Inputs/Day6.txt', 'r') as input_file:
    lines = [line for line in input_file]

problems = [[op] for op in re.findall('[*+]\\s+', lines[-1])]
for line in lines[0:-1]:
    j = 0
    for problem in problems:
        width = len(problem[0])
        problem.append(line[j:j+width])
        j += width
        
sum1 = 0
for problem in problems:
    # print(problem)
    if problem[0].startswith('+'):
        sum1 += sum([int(num) for num in problem[1:]])
    elif problem[0].startswith('*'):
        sum1 += math.prod([int(num) for num in problem[1:]])    
print(f'1. Answer is: {sum1}') # 5784380717354

sum2 = 0
for problem in problems:
    transform = []
    for i in range(len(problem[0])):
        num = ''.join([str[i] for str in problem[1:]])
        if num.strip() != '':
            transform.append(num)
    # print(transform)
    if problem[0].startswith('+'):
        sum2 += sum([int(num) for num in transform])
    elif problem[0].startswith('*'):
        sum2 += math.prod([int(num) for num in transform])   
print(f'2. Answer is: {sum2}') # 7996218225744
# time: 00:44:19