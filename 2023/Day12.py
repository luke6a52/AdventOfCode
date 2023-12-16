with open('2023/Inputs/Day12.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

def getNextOptions(options, groups):
    nextOptions = {}
    minLen = sum(groups) + len(groups[1:])
    maxSum = sum(groups[1:])
    group = groups[0]
    for option, count in options.items():
        for j, spring in enumerate(option):
            # if ( re.match('^[?\.]{' + j + '}[?#]{' + group + '}[?\.]?(.{' + sum(groups[1:]) + len(groups[2:]) + ',})$', option) ):
            if (len(option)-j >= minLen and
                all([c == '?' or c == '.' for c in option[:j]]) and
                all([c == '?' or c == '#' for c in option[j:j+group]]) and
                all([c == '?' or c == '.' for c in option[j+group:j+group+1]]) and
                sum([c == '#' for c in option[j+group+1:]]) <= maxSum):
                remaining = option[j+group+1:]
                y = min(remaining.index('?') if '?' in remaining else len(remaining),
                        remaining.index('#') if '#' in remaining else len(remaining))
                nextOptions[remaining[y:]] = nextOptions.get(remaining[y:], 0) + 1*count
    return nextOptions

sum1 = 0
sum2 = 0
for i, line in enumerate(lines):
    springs, groups = line.split()

    groups1 = [int(n) for n in groups.split(',')]
    options1 = {springs: 1}
    for k, group in enumerate(groups1):
        options1 = getNextOptions(options1, groups1[k:])
    sum1 += sum(options1.values())

    groups2 = groups1 * 5
    options2 = {'?'.join([springs] * 5): 1}
    for k, group in enumerate(groups2):
        options2 = getNextOptions(options2, groups2[k:])
    print(options2)
    sum2 += sum(options2.values())
print(f'1. Answer is: {sum1}') # 7843
print(f'2. Answer is: {sum2}') # 10153896718999