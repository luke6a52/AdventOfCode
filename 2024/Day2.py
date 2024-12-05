import re

with open('2024/Inputs/Day2.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

sum1 = 0
sum2 = 0
sum3 = 0
for line in lines:
    nums = [int(num) for num in re.findall('\d+', line)]
    diffs = [b - a for a, b in zip(nums[:-1], nums[1:])]
    pos = [diff > 0 and diff <= 3 for diff in diffs]
    neg = [diff < 0 and diff >= -3 for diff in diffs]
    if all(pos) or all(neg):
        sum1 += 1
        sum2 += 1
        sum3 += 1
    else:
        safe2 = False
        for i in range(len(nums)):
            nums2 = nums[:i] + nums[i+1:]
            diffs2 = [b - a for a, b in zip(nums2[:-1], nums2[1:])]
            safe2 = all([diff > 0 and diff <= 3 for diff in diffs2]) or all([diff < 0 and diff >= -3 for diff in diffs2])
            if safe2:
                sum2 += 1
                break

        safe3 = False
        if pos.count(False) == 1: # Doesn't catch 2 bad diffs next to each other that would cancel each other out
            i = pos.index(False)
            if i > 0 and i < len(diffs) - 1:
                diff_a = diffs[i-1] + diffs[i]
                diff_b = diffs[i] + diffs[i+1]
                safe3 = (diff_a > 0 and diff_a <= 3) or (diff_b > 0 and diff_b <= 3)
            else:
                safe3 = True
        if not safe3 and neg.count(False) == 1: # Same
            i = neg.index(False)
            if i > 0 and i < len(diffs) - 1:
                diff_a = diffs[i-1] + diffs[i]
                diff_b = diffs[i] + diffs[i+1]
                safe3 = (diff_a < 0 and diff_a >= -3) or (diff_b < 0 and diff_b >= -3)
            else:
                safe3 = True
        if safe3:
            sum3 += 1
        if safe2 and not safe3:
            print(f'{nums} -> {diffs} -> {i} -> {diffs2}')

print(f'1. Answer is: {sum1}') # 490
print(f'2. Answer is: {sum2}') # 536
print(f'2. Answer is: {sum3}') # 528 too low