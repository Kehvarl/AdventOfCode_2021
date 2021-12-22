from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]

reactor = set()

settings = []
for line in content:
    # on x=10..12,y=10..12,z=10..12
    state, line = line.split(' ')
    x, y, z = line.strip().split(',')
    x1, x2 = x[2:].split('..')
    y1, y2 = y[2:].split('..')
    z1, z2 = z[2:].split('..')
    if state == 'on':
        state = 1
    else:
        state = 0

    x1 = max(int(x1), -50)
    x2 = min(int(x2), 50)
    y1 = max(int(y1), -50)
    y2 = min(int(y2), 50)
    z1 = max(int(z1), -50)
    z2 = min(int(z2), 50)

    for x in range(int(x1), int(x2)+1):
        for y in range(int(y1), int(y2)+1):
            for z in range(int(z1), int(z2)+1):
                if state == 1:
                    reactor.add((x, y, z))
                else:
                    reactor.discard((x, y, z))

print(len(reactor))

