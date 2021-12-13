from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]

max_x = 0
max_y = 0
sheet = defaultdict(int)
folds = []

folding = False
for line in content:
    if not folding:
        if line.strip() == "":
            folding = True
            continue
        x, y = line.strip().split(',')
        x = int(x)
        y = int(y)
        sheet[x, y] = 1
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    else:
        discard, fold = line.strip().split("fold along ")
        a, v = fold.split('=')
        folds.append((a, int(v)))


def display():
    for y in range(max_y + 1):
        line = ""
        for x in range(max_x + 1):
            if sheet[(x, y)] > 0:
                line += "#"
            else:
                line += "."
        print(line)


def count():
    total = 0
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if sheet[(x, y)] > 0:
                total += 1
    return total


def fold_x(x):
    global max_x
    global sheet
    for y in range(max_y + 1):
        for i, x2 in enumerate(range(x, max_x + 1)):
            sheet[(x2-(2*i), y)] += sheet[(x2, y)]
    max_x = x - 1


def fold_y(y):
    global max_y
    global sheet
    for i, y2 in enumerate(range(y, max_y + 1)):
        for x in range(max_x + 1):
            sheet[(x, y2-(2*i))] += sheet[(x, y2)]
    max_y = y -1


#for a, v in folds:
a,v = folds[0]
if a == 'y':
    fold_y(v)
elif a == 'x':
    fold_x(v)

print(count())
