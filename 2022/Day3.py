with open('2022/Inputs/Day3.txt', 'r') as input_file:
    lines = input_file.readlines()
sacks = [line.rstrip() for line in lines]

priority1 = 0
for sack in sacks:
    left = sack[:int(len(sack)/2)]
    right = sack[int(len(sack)/2):]
    for item in left:
        if item in right:
            priority1 += (ord(item)-38)%58
            break
print(f'1. Answer is: {priority1}') # 7863   23m 8s

priority2 = 0
for i in range(0,len(sacks),3):
    first = sacks[i]
    second = sacks[i+1]
    third = sacks[i+2]
    for item in first:
        if item in second and item in third:
            priority2 += (ord(item)-38)%58
            break
print(f'2. Answer is: {priority2}') # 2488   30m 4s