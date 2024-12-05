import re

with open('2024/Inputs/Day1.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

left = []
right = []
for line in lines:
    nums = [int(num) for num in re.findall('\d+', line)]
    left.append(nums[0])
    right.append(nums[1])
left.sort()
right.sort()

sum1 = 0
for i, l in enumerate(left):
    r = right[i]
    sum1 += abs(r - l)
print(f'1. Answer is: {sum1}') # 1110981

sum2 = 0
r_count = {}
for r in right:
    if r in r_count:
        r_count[r] += 1
    else:
        r_count[r] = 1
    #print(f'{r} -> {r_count}')
for l in left:
    if l in r_count:
        sum2 += l * r_count[l]
print(f'2. Answer is: {sum2}') # 24869388