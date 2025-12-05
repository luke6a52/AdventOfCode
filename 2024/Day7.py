import re

with open('2024/Inputs/Day7.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

def checkOperator1(goal, nums):
    # print(nums)
    if sum(nums) == goal:
        return True
    elif len(nums) < 2:
        return False
    else:
        mul = [nums[0] * nums[1]] + nums[2:]
        add = [nums[0] + nums[1]] + nums[2:]
        return checkOperator1(goal, mul) or checkOperator1(goal, add)

def checkOperator2(goal, nums):
    # print(nums)
    if sum(nums) == goal:
        return True
    elif len(nums) < 2:
        return False
    else:
        mul = [nums[0] * nums[1]] + nums[2:]
        cat = [int(f'{nums[0]}{nums[1]}')] + nums[2:]
        add = [nums[0] + nums[1]] + nums[2:]
        return checkOperator2(goal, mul) or checkOperator2(goal, cat) or checkOperator2(goal, add)

sum1 = 0
sum2 = 0
for line in lines:
    nums = [int(num) for num in re.findall('\d+', line)] # type: ignore
    if checkOperator1(nums[0], nums[1:]):
        sum1 += nums[0]
    if checkOperator2(nums[0], nums[1:]):
        sum2 += nums[0]
print(f'1. Answer is: {sum1}') # 5702958180383
print(f'2. Answer is: {sum2}') # 92612386119138