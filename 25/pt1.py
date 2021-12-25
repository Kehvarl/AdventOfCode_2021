from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]


map = []

for line in content:
    map.append(list(line.strip()))


def get_right(map, x, y):
    if y < len(map) and x+1 < len(map[0]):
        return map[y][x+1]
    else:
        return map[y][0]



def get_down(map, x, y):
    if y+1 < len(map) and x < len(map[0]):
        return map[y+1][x]
    else:
        return map[0][x]


def step_right(map):
    new_map = [['.' for _ in range(len(list(map[0])))] for _ in range(len(map))]

    for r, line in enumerate(map):
        for c, cell in enumerate(line):
            if cell == '>':
                if get_right(map, c, r) == '.':
                    if c+1 < len(map[0]):
                        new_map[r][c+1] = cell
                    else:
                        new_map[r][0] = cell
                else:
                    new_map[r][c] = cell
            elif cell == 'v':
                new_map[r][c] = cell

    return new_map


def step_down(map):
    new_map = [['.' for _ in range(len(list(map[0])))] for _ in range(len(map))]
    for r, line in enumerate(map):
        for c, cell in enumerate(line):
            if cell == 'v':
                if get_down(map, c, r) == '.':
                    if r + 1 < len(map):
                        new_map[r + 1][c] = cell
                    else:
                        new_map[0][c] = cell
                else:
                    new_map[r][c] = cell
            elif cell == '>':
                new_map[r][c] = cell
    return new_map


def print_board(map):
    for line in map:
        print(''.join(line))


steps = 0
while True:
    new_map = step_down(step_right(map))
    steps += 1
    if new_map == map:
        break
    map = new_map
    # print_board(map)
    print()
    print()


print(steps)
