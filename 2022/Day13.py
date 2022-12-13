import functools

with open('2022/Inputs/Day13.txt', 'r') as input_file:
    input_pairs = input_file.read().split('\n\n')

pairs = []
for input in input_pairs:
    lines = input.split('\n')
    vars = {}
    exec(f'left = {lines[0]}\nright = {lines[1]}', {}, vars)
    pairs.append((vars['left'], vars['right']))

def compare(left, right):
    if(isinstance(left, int) and isinstance(right, int)): return right - left
    if(isinstance(left, int) ): left = [left]
    if(isinstance(right, int)): right = [right]
    for i in range(min(len(left), len(right))):
        comp = compare(left[i], right[i])
        if(comp != 0): return comp
    return len(right) - len(left)

answer1 = 0
for i, pair in enumerate(pairs):
    if(compare(pair[0], pair[1]) > 0): 
        answer1 += i+1
print(f'1. Answer is: {answer1}') # 5555   56m

packets = [[[2]], [[6]]]
for pair in pairs:
    packets.append(pair[0])
    packets.append(pair[1])
packets.sort(key=functools.cmp_to_key(compare), reverse=True)

answer2 = (packets.index([[2]])+1) * (packets.index([[6]])+1)
print(f'2. Answer is: {answer2}') # 22852   1h 14m