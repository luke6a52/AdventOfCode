with open('2022/Day1.txt', 'r') as input_file:
    lines = input_file.readlines()
calories = [line.rstrip() for line in lines]

elves = [0]
for cal in calories:
    if cal == '':
        elves.append(0)
    else:
        elves[-1] += int(cal)
print(f'1. Answer is: {max(elves)}') # 74394

maxElves = [0,0,0]
for i in range(3):
    maxElves[i] = max(elves)
    elves.remove(maxElves[i])
print(f'2. Answer is: {sum(maxElves)}') # 212836