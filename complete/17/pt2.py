from collections import defaultdict
from pprint import pprint

Testing = False

with open("input.txt") as f:
    content = f.readline().strip()
    # content = [int(x) for x in f.readlines()]


rx, ry = content[13:].split(', ')
x1, x2 = rx[2:].split('..')
y1, y2 = ry[2:].split('..')
x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)
sx = 0
sy = 0

print(rx, x1, x2)
print(ry, y1, y2)


with open("compare.txt") as f:
    content = f.readline().strip()
pairs = content.split(' ')
test = set()
count = 0
for p in pairs:
    count += 1
    if p == '':
        continue
    a, b = p.split(',')
    test.add((int(a), int(b)))


def step(sx, sy, vx, vy):
    sx += vx
    sy += vy
    if vx > 0:
        vx -=1
    elif vx < 0:
        vx += 1
    vy -= 1
    return sx, sy, vx, vy


def check(sx, sy,  x1, x2, y1, y2):
    return sx in range(min(x1, x2), max(x1, x2)+1) and \
           sy in range(max(y1, y2), min(y1, y2) - 1, -1)


valid = set()
max_y = 0
for x in range(300):
    for y in range(-150, 200):
        rmy = 0
        wx, wy = sx, sy
        vx, vy = x, y
        while True:
            wx, wy, vx, vy = step(wx, wy, vx, vy)
            rmy = max(rmy, wy)
            if check(wx, wy, x1, x2, y1, y2):
                max_y = max(rmy, max_y)
                valid.add((x, y))
                break
            if wx > max(x1, x2) or wy < min(y1, y2):
                if Testing and (x, y) in test:
                    print(x1, x2, wx, y1, y2, wy)
                break

print(max_y)
print(len(valid))

