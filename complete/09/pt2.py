from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]


map = []
for line in content:
    map.append([int(x) for x in list(line.strip())])

height = len(map)
width = len(map[0])
lows = []


def check(x, y):
    test = map[y][x]
    if x > 0:
        if map[y][x-1] <= test:
            return False
    if x < width-1:
        if map[y][x+1] <= test:
            return False
    if y > 0:
        if map[y-1][x] <= test:
            return False
    if y < height-1:
        if map[y+1][x] <= test:
            return False
    return True


for r in range(height):
    for c in range(width):
        if check(c, r):
            lows.append((c, r, map[r][c]))

# print(lows)


def get_val(x, y):
    if 0 <= x < width and 0 <= y < height:
        return map[y][x]
    else:
        return False


basins = []
sizes = []
for x, y, v in lows:
    basin = set()
    basin.add((x, y))
    testing = set()
    testing.add((x, y))
    while len(testing) > 0:
        x1, y1 = testing.pop()
        v1 = map[y1][x1]
        for x2, y2 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            v2 = get_val(x1+x2, y1+y2)
            if v2 and v2 < 9 and v2 > v1 and (x1+x2, y1+y2) not in basin:
                basin.add((x1+x2, y1+y2))
                testing.add((x1+x2, y1+y2))
    basins.append(basin)
    sizes.append(len(basin))

print(sorted(sizes, reverse=True)[:3])
total = 1
for s in sorted(sizes, reverse=True)[:3]:
    total *= s
print(total)
