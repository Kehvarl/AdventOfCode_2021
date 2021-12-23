from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    # content = [int(x) for x in f.readlines()]

reactor = set()

steps = []
for line in content:
    # on x=10..12,y=10..12,z=10..12
    state, line = line.split(' ')
    state = 1 if state == "on" else 0

    x, y, z = line.strip().split(',')
    x1, x2 = [int(a) for a in x[2:].split('..')]
    y1, y2 = [int(a) for a in y[2:].split('..')]
    z1, z2 = [int(a) for a in z[2:].split('..')]
    xr = range(x1, x2+1)
    yr = range(y1, y2+1)
    zr = range(z1, z2+1)
    steps.append((state, xr, yr, zr))


def get_subrange(crange, low, high):
    c0 = crange[0]
    c1 = crange[-1]
    if c1 < low:
        return []
    elif c0 > high:
        return []
    c0 = max(c0, low)
    c1 = max(c1, low)
    c0 = min(c0, high)
    c1 = min(c1, high)
    return range(c0, c1+1)


def count_in_cube(step, rest):
    _, xr, yr, zr = step
    total = len(xr) * len(yr) * len(zr)

    overlap = []
    ref_val = 0

    for step in rest:
        state, xr2, yr2, zr2 = step

        cxr = get_subrange(xr2, xr[0], xr[-1])
        cyr = get_subrange(yr2, yr[0], yr[-1])
        czr = get_subrange(zr2, zr[0], zr[-1])

        if len(cxr) == 0 or len(cyr) == 0 or len(czr) == 0:
            continue

        overlap.append((state, cxr, cyr, czr))
        ref_val += len(cxr) * len(cyr) * len(czr)

    for i, ovr in enumerate(overlap):
        total -= count_in_cube(ovr, overlap[i+1:])

    return total


on = 0

for i, step in enumerate(steps):
    state, xr, yr, zr = step
    if state == 0:
        continue
    on += count_in_cube(step, steps[i+1:])

print(on)
