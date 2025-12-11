import re

with open('2025/Inputs/Day11.txt', 'r') as input_file:
    lines = [line.rstrip() for line in input_file]

devices = dict()
for line in lines:
    names = re.findall('\\w+', line)
    devices[names[0]] = names[1:]

# # Count connections into each device
# # (I thought this would be slower and I would need to abort whenever I encountered an already processed node, 
# #  then calculate the combinations in another pass, waiting to process nodes until I had processed all connections in)
# sum1 = 0
# path = {'you':1}
# def addConnections(name):
#     for connect in devices[name]:
#         path[connect] = path.get(connect, 0) + 1
#         if connect != 'out':
#             addConnections(connect)
# addConnections('you')
# # print(path)
# sum1 = path['out']
# print(f'1. Answer is: {sum1}') # 

sum2 = {'dac':0, 'fft':0, 'out':0}
def addSvrConnections(name, goal):
    for connect in devices[name]:
        if connect == goal:
            sum2[goal] += 1
        elif connect != 'out':
            addSvrConnections(connect, goal)
addSvrConnections('svr', 'dac')
print(f'2. Answer is: {sum2}') # 
# time: 03:00:00