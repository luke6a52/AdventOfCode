with open('2022/Inputs/Day15.txt', 'r') as input_file:
    jets = input_file.read()

blocks = [
    [[1,1,1,1]],
    [[0,1,0], [1,1,1], [0,1,0]],
    [[1,1,1], [0,0,1], [0,0,1]],
    [[1], [1], [1], [1]],
    [[1,1], [1,1]]
]

tower = [1,1,1,1,1,1,1,1,1]
for i in range(2022):
    block = blocks[i%5]
    # while True:

print(f'1. Answer is: {len(tower)}') # ??   ~20m
#print(f'2. Answer is: {???}') # ??   ?m