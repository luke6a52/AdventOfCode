import re

with open('2023/Inputs/Day1.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

sum1 = 0
for line in lines:
    nums = re.findall('\d', line)
    sum1 += int(nums[0] + nums[-1])
print(f'1. Answer is: {sum1}') # 54450

sum2 = 0
words = {'on': '1', 'tw': '2', 'thre': '3', 'four': '4', 'fiv': '5', 'six': '6', 'seve': '7', 'eigh': '8', 'nin': '9'}
for line in lines:
    nums = re.findall('\d|on(?=e)|tw(?=o)|thre(?=e)|four|fiv(?=e)|six|seve(?=n)|eigh(?=t)|nin(?=e)', line)
    if nums[0] in words:
        nums[0] = words[nums[0]]
    if nums[-1] in words:
        nums[-1] = words[nums[-1]]
    sum2 += int(nums[0] + nums[-1])
print(f'2. Answer is: {sum2}') # 54265