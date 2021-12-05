
with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]


segments = []
for line in content:
    start, end = line.split(" -> ")
    sx, sy = [int(i) for i in start.split(",")]
    ex, ey = [int(i) for i in end.split(",")]
    segments.append([sx, sy, ex, ey])


grid = {}
def plot(x, y):
    if not grid.get((x, y), None):
        grid[(x, y)] = 1
    else:
        grid[(x, y)] += 1


for line in segments:
    sx, sy, ex, ey = line
    x, y = sx, sy
    while True:
        plot(x, y)
        if (x, y) == (ex, ey):
            break
        if ex > sx:
            x += 1
        elif ex < sx:
            x -= 1
        if ey > sy:
            y += 1
        elif ey < sy:
            y -= 1


sum = 0
for i in grid:
    if grid[i] > 1:
        sum += 1

print(sum)
