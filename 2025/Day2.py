import re

with open('2025/Inputs/Day2.txt', 'r') as input_file:
    line = [line.rstrip() for line in input_file][0]

sum1 = 0
sum2 = []
for span in line.split(','):
    # print(span)
    numstrs = re.findall('\d+', span) # type: ignore
    len0 = len(numstrs[0])
    len1 = len(numstrs[1])
    num0 = int(numstrs[0])
    num1 = int(numstrs[1])

    for i in range(2, len1+1):
        # ensure equal length divisible by i
        if len0%i == 0 and len1%i == 0:
            leng = len0//i
            start0 = int(numstrs[0][0:leng])
            start1 = int(numstrs[1][0:leng])
        elif len0%i == 0:
            leng = len0//i
            start0 = int(numstrs[0][0:leng])
            start1 = 10**(leng)-1
        elif len1%i == 0:
            leng = len1//i
            start0 = 10**(leng-1)
            start1 = int(numstrs[1][0:leng])
        else:
            continue

        # count unique matches
        for start in range(start0, start1+1):
            num = 0
            for j in range(i):
                num += start * 10**(leng*j)
            if num0 <= num <= num1:
                if i == 2:
                    sum1 += num
                if num not in sum2:
                    # print(num)
                    sum2.append(num)

print(f'1. Answer is: {sum1}') # 34826702005
print(f'2. Answer is: {sum(sum2)}') # 43287141963
# time: 01:12:50