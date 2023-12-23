import re

with open('2020/Inputs/Day4.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

# Setup
passports = [{}]
for i, line in enumerate(lines):
    if line == '':
        passports.append({})
    else:
        fields = line.split(' ')
        for field in fields:
            key, val = field.split(':')
            passports[-1][key] = val

# Part 1
sum1 = 0
for passport in passports:
    count = 0
    for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if key in passport:
            count += 1
    if count == 7:
        sum1 += 1
print(f'1. Answer is: {sum1}') # 237

# Part 2
sum2 = 0
for passport in passports:
    count = 0
    if 'byr' in passport and 1920 <= int(passport['byr']) <= 2002:
        count += 1
    if 'iyr' in passport and 2010 <= int(passport['iyr']) <= 2020:
        count += 1
    if 'eyr' in passport and 2020 <= int(passport['eyr']) <= 2030:
        count += 1
    if 'hgt' in passport:
        if passport['hgt'][-2:] == 'cm' and 150 <= int(passport['hgt'][:-2]) <= 193:
            count += 1
        elif passport['hgt'][-2:] == 'in' and 59 <= int(passport['hgt'][:-2]) <= 76:
            count += 1
    if 'hcl' in passport and re.match('^#[0-9a-f]{6}$', passport['hcl']):
        count += 1
    if 'ecl' in passport and passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        count += 1
    if 'pid' in passport and re.match('^[0-9]{9}$', passport['pid']):
        count += 1
    if count == 7:
        sum2 += 1
print(f'2. Answer is: {sum2}') # 172