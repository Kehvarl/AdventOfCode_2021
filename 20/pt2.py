from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]


algo = [0 if x == '.' else 1 for x in list(content[0].strip())]

image = defaultdict(int)

row0 = 0
col0 = 0
width = len(content[2])
height = len(content[2:])

for r in range(len(content[2:])):
    line = content[2+r].strip()
    for c in range(len(line)):
        image[(r, c)] = 0 if line[c] == '.' else 1


def get_neighbors(r, c, image, i):
    ret = ""
    for nr in range(r-1, r+2):
        for nc in range(c-1, c+2):
            if nr < row0 or nr > height or nc < col0 or nc > width:
                if i % 2 == 0:
                    ret += '1'
                else:
                    ret += '0'
            else:
                ret += str(image[(nr, nc)])
    return ret


def get_pixel(val):
    return algo[int(val, 2)]


def step(image, i):
    newimage = defaultdict(int)
    for r in range(row0-3, height+4):
        for c in range(col0-3, width+4):
            newimage[(r, c)] = get_pixel(get_neighbors(r, c, image, i))
    return newimage


for i in range(50):
    print(i)
    image = step(image, i)
    row0 -= 1
    col0 -= 1
    height += 1
    width += 1


# print(image)
total = 0

for r in range(row0+1, height):
    line = ""
    for c in range(col0+1, width):
        total += image[(r, c)]
        if image[(r, c)] == 1:
            line += '#'
        else:
            line += '.'
    print(line)

print(total)
