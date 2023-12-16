with open('2023/Inputs/Day12.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]
    
def checkOption(option, groups):
    groups = groups.copy()
    count = 0
    for j, spring in enumerate(option):
        if spring == '#':
            count += 1
            if len(groups) == 0 or count > groups[0]:
                return False
        elif spring == '.':
            if count > 0:
                if len(groups) == 0 or count < groups[0]:
                    return False
                groups.pop(0)
            count = 0
        else:
            return len(groups) == 0 or (len(option) - j) >= (len(groups) - 1) + (sum(groups) - count)
    return len(groups) == 0 or (len(groups) == 1 and count == groups[0])

def countOptions(option, groups):
    option = option.copy()
    count = 0
    if '?' in option:
        j = option.index('?')
        for c in ('.', '#'):
            option[j] = c
            if checkOption(option, groups):
                count += countOptions(option, groups)
    else:
        count = 1
    return count

options1 = []
options2 = []
for i, line in enumerate(lines):
    springs, groups = line.split()

    option1 = [c for c in springs]
    groups1 = [int(n) for n in groups.split(',')]
    options1.append(countOptions(option1, groups1))

    option2 = option1 + ['?'] + option1
    groups2 = groups1 + groups1
    temp2 = countOptions(option2, groups2)
    options2.append((temp2 // options1[-1])**4 * options1[-1])
print(f'1. Answer is: {sum(options1)}') # 7843
print(f'2. Answer is: {sum(options2)}') # 4901045761218 too low
    
# 1 group  in min+3 space: 1+1+1+1  = 4/(1)
# 2 groups in min+3 space: 1+2+3+4  = 4*(4+1)/(1*2)
# 3 groups in min+3 space: 1+3+6+10 = 4*(4+1)*(4+2)/(1*2*3) = prod( (4+i)/(i+1) )
    
# ????                      1,1                 -> 1+2                  = 3     12  = 3*4
# ?????????                 1,1,1,1             -> 1+4+10               = 15    69  = 3*23
# ??????????????            1,1,1,1,1,1         -> 1+6+21+56            = 84    411 = 3*137     (15/3)**2 * 3 = 75        84 -   75 =   9   = 3*3
# ???????????????????       1,1,1,1,1,1,1,1     -> 1+8+36+120+330       = 495   2310= 3*770     (15/3)**3 * 3 = 375      495 -  375 = 120   = 2*3*4*5
# ????????????????????????  1,1,1,1,1,1,1,1,1,1 -> 1+10+21+56+715+2002  = 2805     =2*3*5*7*11  (15/3)**4 * 3 = 1875    2805 - 1875 = 930   = 2*3*5*31
# my algorithm says: (15/3)**2 * 3 = 75 not 84

# 1  2  3  4   5   6   7   8    9   10
# 1  3  6 10  15  21  28  36   45   55
# 1  4 10 20  35  56  84 120  165  220
# 1  5 15 35  70 126 210 330  495  715
# 1  6 21 56 126 252 462 792 1287 2002