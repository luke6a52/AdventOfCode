with open('2020/Day2.txt', 'r') as input_file:
    lines = input_file.readlines()

valid1 = 0
valid2 = 0
for line in lines:
    policy, password = line.split(': ', 1)
    character = policy[-1]
    minimum, maximum = [int(num) for num in policy[0:-2].split('-', 1)]
    chars1 = password.count(character)
    if chars1 >= minimum and chars1 <= maximum: valid1 += 1
    chars2 = [password[minimum-1], password[maximum-1]].count(character)
    if chars2 == 1: valid2 += 1
print(f'1. Answer is {valid1}')
print(f'2. Answer is {valid2}')