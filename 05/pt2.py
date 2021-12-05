from bresenham import bresenham

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
    for cell in bresenham(sx, sy, ex, ey):
        plot(cell[0], cell[1])

sum = 0
for i in grid:
    if grid[i] > 1:
        sum += 1

print(sum)
