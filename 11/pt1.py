from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]

octopodes = {}
for r, row in enumerate(content):
    for c, col in enumerate((row.strip())):
        octopodes[(r, c)] = int(col)


def flash(r, c):
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == dc == 0:
                continue
            if r + dr < 0 or r + dr > 9:
                continue
            if c + dc < 0 or c + dc > 9:
                continue
            octo = octopodes[(r + dr, c + dc)]
            if octo > -1:
                octo += 1
            if octo > 9:
                octopodes[(r + dr, c + dc)] = -1
                flash(r + dr, c + dc)
                octo = -1
            octopodes[(r + dr, c + dc)] = octo


def count_flashes():
    flashes = 0
    for r in range(10):
        for c in range(10):
            if octopodes[(r, c)] == -1:
                flashes += 1
                octopodes[(r, c)] = 0
    return flashes

def doflash():
    for r in range(10):
        for c in range(10):
            octo = octopodes[(r,c)]
            if octo > 9:
                octopodes[(r, c)] = -1
                flash(r, c)
                octo = -1
            octopodes[(r, c)] = octo


def step():
    for r in range(10):
        for c in range(10):
            octopodes[(r, c)] += 1
    doflash()

f = 0
for i in range(100):
    step()
    f += count_flashes()
    print(f)

print(f)
