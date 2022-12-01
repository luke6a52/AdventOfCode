with open('2020/Day1.txt', 'r') as input_file:
    lines = input_file.readlines()
numbers = [int(line) for line in lines]

for i in range(len(numbers)):
    first = numbers[i]
    second = 2020 - first
    if second in numbers[i+1:-1]:
        print(f'1. First is: {first}')
        print(f'1. Second is: {second}')
        print(f'1. Answer is: {first * second}')
        break
    
for i in range(len(numbers)):
    first = numbers[i]
    for j in range(i+1, len(numbers)):
        second = numbers[j]
        third = 2020 - first - second
        if third in numbers[j+1:-1]:
            print(f'2. First is: {first}')
            print(f'2. Second is: {second}')
            print(f'2. Second is: {third}')
            print(f'2. Answer is: {first * second * third}')
            break