from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    # content = [int(x) for x in f.readlines()]

map = []
for line in content:
    l = [int(x) for x in list(line.strip())]
    map.append(l)

height = len(map)
width = len(map[0])

visited = set()
queue = [(0, 0, 0)]
destination = (width - 1, height - 1)
pathcost = {}

neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_neighbors(x, y):
    n = []
    for dx, dy in neighbors:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < width and 0 <= ny < width:
            n.append((nx, ny, map[ny][nx]))
    return n


while True:
    cost, x, y = queue[0]
    if (x, y) == destination:
        print(cost)
        break
    queue = queue[1:]

    for nx, ny, nc in get_neighbors(x, y):
        newcost = cost + nc
        if (nx, ny) in pathcost and pathcost[(nx, ny)] <= newcost:
            continue
        pathcost[(nx, ny)] = newcost
        queue.append((newcost, nx, ny))
    queue = sorted(queue)






