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

risk = 0
for point in lows:
    x, y, r = point
    risk += r + 1

print(risk)
