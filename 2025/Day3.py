import re

with open('2025/Inputs/Day3.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

sum1 = 0
sum2 = 0
for line in lines:
    nums = [int(num) for num in re.findall('\\d', line)]

    best1 = [0,1]
    best2 = [0,1,2,3,4,5,6,7,8,9,10,11]
    for i, num in enumerate(nums):

        for j in range(2):
            if i <= best1[j]:
                break
            if num > nums[best1[j]] and i+1-j < len(nums):
                for k in range(2-j):
                    best1[j+k] = i+k
                break

        for j in range(12):
            if i <= best2[j]:
                break
            if num > nums[best2[j]] and i+11-j < len(nums):
                for k in range(12-j):
                    best2[j+k] = i+k
                break

    combo1 = 0
    for j in range(2):
        combo1 += nums[best1[j]] * 10**(1-j)
    # print(combo1)
    sum1 += combo1

    combo2 = 0
    for j in range(12):
        combo2 += nums[best2[j]] * 10**(11-j)
    # print(combo2)
    sum2 += combo2

print(f'1. Answer is: {sum1}') # 17034
print(f'2. Answer is: {sum2}') # 168798209663590
# time: 00:36:55