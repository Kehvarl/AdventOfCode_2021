

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]


segments = []
for line in content:
    start, end = line.split(" -> ")
    sx, sy = [int(i) for i in start.split(",")]
    ex, ey = [int(i) for i in end.split(",")]
    if sx == ex or sy == ey:
        segments.append([sx, sy, ex, ey])

grid = {}
for line in segments:
    sx, sy, ex, ey = line
    if sx == ex:
        s = min(sy, ey)
        e = max(sy, ey)
        for y in range(s, e+1):
            if not grid.get((sx, y), None):
                grid[(sx, y)] = 1
            else:
                grid[(sx, y)] += 1
    elif sy == ey:
        s = min(sx, ex)
        e = max(sx, ex)
        for x in range(s, e+1):
            if not grid.get((x, sy), None):
                grid[(x, sy)] = 1
            else:
                grid[(x, sy)] += 1

sum = 0
for i in grid:
    if grid[i] > 1:
        sum += 1

print(sum)
