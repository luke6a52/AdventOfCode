import re

with open('2025/Inputs/Day10.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

sum1 = 0
for line in lines:
    goal = [char=='#' for char in line[1:line.index(']')]]
    buttons = [[int(num) for num in button[1:-1].split(',')] for button in re.findall('\\(.*?\\)', line)]
    combos = [[button] for button in buttons]
    while len(combos) > 0:
        combo = combos.pop(0)
        lights = [False] * len(goal)
        for button in combo:
            for i in button:
                lights[i] = not lights[i]
        if lights == goal:
            # print(f'{len(combo)}: {combo}')
            sum1 += len(combo)
            break
        else:
            for button in buttons:
                new = combo + [button]
                new.sort()
                if button not in combo and new not in combos:
                    combos.append(new)
print(f'1. Answer is: {sum1}') # 436

# maybe get every combo of buttons that includes the biggest number without busting,
# then for each of those, check the other buttons exhaustively, breadth-first
# track buttons by number of pushes in a dict
sum2 = 0
for line in lines:
    goal = [int(num) for num in line[line.index('{')+1:-1].split(',')]
    buttons = [tuple([int(num) for num in button[1:-1].split(',')]) for button in re.findall('\\(.*?\\)', line)]
    combos = []
    peak = goal.index(max(goal))
    buttons_w = []
    buttons_wo = []
    for button in buttons:
        if peak in button:
            buttons_w.append(button)
            combos.append({button:1})
        else:
            buttons_wo.append(button)
    while len(combos) > 0:
        combo = combos.pop(0)
        jolts = [0] * len(goal)
        for button in combo.keys():
            for i in button:
                jolts[i] += combo[button]
        if jolts == goal:
            print(f'{sum(combo.values())}: {combo}')
            sum2 += sum(combo.values())
            break
        elif any([jolts[i] > goal[i] for i in range(len(goal))]):
            continue
        else:
            for button in buttons_w:
                new = combo.copy()
                new[button] = new.get(button, 0) + 1
                if new not in combos:
                    combos.append(new)
        print(f'{len(combos)}: {combos[-1]}') # still way too many options: ~1E12
print(f'2. Answer is: {sum2}') # 
# time: 03:00:00 so far