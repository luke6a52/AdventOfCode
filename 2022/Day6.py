with open('2022/Inputs/Day6.txt', 'r') as input_file:
    line = input_file.read()

last_match = 0
answer1 = 0
answer2 = 0
for i in range(len(line)):
    try:
        last_match = max(last_match, i-1 - line[i-1:max(0,i-13):-1].index(line[i]))
    except(ValueError):
        pass

    if(answer1 == 0 and i - last_match >= 4):
        answer1 = i+1
    if(answer2 == 0 and i - last_match >= 14):
        answer2 = i+1
        break
print(f'1. Answer is: {answer1}') # 1848   24m 20s
print(f'2. Answer is: {answer2}') # 2308   25m 38s