import re
import math
import helpers

with open('2023/Inputs/Day7.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

sum1 = 0
sum2 = 0
for i, line in enumerate(lines):
    sum1 += 1
print(f'1. Answer is: {sum1}') #
print(f'2. Answer is: {sum2}') #