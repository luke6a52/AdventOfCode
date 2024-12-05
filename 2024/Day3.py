import re

with open('2024/Inputs/Day3.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]
line = ''.join(lines)

pairs1 = re.findall('mul\((\d{1,3},\d{1,3})\)', line)
sum1 = 0
for pair in pairs1:
    [left, right] = [int(num) for num in re.findall('\d+', pair)]
    sum1 += left * right
print(f'1. Answer is: {sum1}') # 174960292

lines2 = re.findall('(?:^|do\(\)).*?(?:$|don\'t\(\))', line)
pairs2 = []
for line2 in lines2:
    pairs2 += re.findall('mul\((\d{1,3},\d{1,3})\)', line2)
sum2 = 0
for pair in pairs2:
    [left, right] = [int(num) for num in re.findall('\d+', pair)]
    sum2 += left * right
print(f'2. Answer is: {sum2}') # 56275602