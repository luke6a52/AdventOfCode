import math

with open('2023/Inputs/Day20.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

nodes = {}
for i, line in enumerate(lines):
    name, outs = line.split(' -> ')
    outs = outs.split(', ')
    if name[0] == '%':
        nodes[name[1:]] = [False, outs] # Flip Flop
    elif name[0] == '&':
        nodes[name[1:]] = [{}, outs] # Conjunction
    else:
        nodes[name] = [None, outs] # Broadcaster
for name, node in nodes.items():
    for out in node[1]:
        if out in nodes and isinstance(nodes[out][0], dict):
            nodes[out][0][name] = False
states = set()
lowList = []
highList = []
state = tuple([(name, tuple(node[0].items()) if isinstance(node[0], dict) else node[0]) for name, node in nodes.items()])
iters = 1000
sum2 = 0
while state not in states and len(states) < iters: #and sum2 == 0: 
    pulses = [(False, 'broadcaster', out) for out in nodes['broadcaster'][1]] # Broadcaster
    lows = 1 + len(pulses) # Falses
    highs = 0 # Trues
    while len(pulses) > 0:
        pulse = pulses.pop(0)
        if pulse[2] not in nodes:
            if not pulse[0]:
                sum2 = len(states) + 1
                break
            continue
        node = nodes[pulse[2]]
        if isinstance(node[0], bool): # Flip Flop
            if not pulse[0]:
                send = node[0] = not node[0]
                for out in node[1]:
                    pulses.append((send, pulse[2], out))
                if send:
                    highs += len(node[1])
                else:
                    lows += len(node[1])
        else: # Conjunction
            node[0][pulse[1]] = pulse[0]
            send = not all(node[0].values())
            for out in node[1]:
                pulses.append((send, pulse[2], out))    
            if send:
                highs += len(node[1])
            else:
                lows += len(node[1])
        if pulse[0] and pulse[2] == 'vr':
            print(len(states)+1, pulse[2], node[0])
    states.add(state)
    lowList.append(lows)
    highList.append(highs)
    state = tuple([(name, tuple(node[0].items()) if isinstance(node[0], dict) else node[0]) for name, node in nodes.items()])
cycles = iters // len(states)
rem = iters % len(states)
sum1 = (sum(lowList) * cycles + sum(lowList[:rem])) * (sum(highList) * cycles + sum(highList[:rem]))
sum2 = math.lcm(3793, 3929, 4001, 4007) # cycle lengths of each of the four inputs to 'vr' (from manual inspection with iters=10000)
print(f'1. Answer is: {sum1}') # 712543680
print(f'2. Answer is: {sum2}') # 238920142622879

#TODO get rid of all the state tracking and find the LCMs programmatically