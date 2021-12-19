from collections import defaultdict
from pprint import pprint

with open("test.txt") as f:
    content = f.readlines()

scanners = {}
current = None
for line in content:
    line = line.strip()
    if line[0:3] == '---':
        _, n = line.strip('---').strip().split(' ')
        current = int(n)
        scanners[current] = defaultdict(int)
    elif line.strip() == '':
        continue
    else:
        x, y, z = line.strip().split(',')
        x = int(x)
        y = int(y)
        z = int(z)
        scanners[current][(x, y, z)] = 1


for s in scanners:
    print(scanners[s])

