from collections import defaultdict
from pprint import pprint

with open("test1.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]


unique_segments = {
    2: 1,
    3: 7,
    4: 4,
    # 5: [2, 3, 5],
    # 6: [6, 9, 0],
    7: 8
}

segment_map = {
    1: ['a', 'b'],
    2: ['f', 'a', 'g', 'd', 'c'],
    3: ['f', 'a', 'g', 'b', 'c'],
    4: ['e', 'g', 'a', 'b'],
    5: ['f', 'e', 'g', 'b', 'c'],
    6: ['f', 'e', 'g', 'd', 'b', 'c'],
    7: ['f', 'a', 'b'],
    8: ['f', 'e', 'a', 'g', 'd', 'b', 'c'],
    9: ['f', 'e', 'a', 'g', 'b'],
    0: ['f', 'e', 'a', 'd', 'b', 'c']
}
for s in segment_map:
    segment_map[s].sort()


for line in content:
    mapping = {}
    letter_map = {}
    i, o = line.strip().split("|")
    input = i.split(" ")
    output = o.split(" ")

    for i in input:
        if len(i) in unique_segments:
            mapping[unique_segments[len(i)]] = sorted(list(i))

    print(mapping)

    for k, m in mapping.items():
        for l in m:
            if l not in letter_map:
                letter_map[l] = set()
            letter_map[l].add(l)

# 1:       (top-right, bottom-right)
# 7 and 1: top
# 4 and 1: (top-left, center)
# 4 and 8: (bottom-left, bottom), top-left, center

# 3: 7 and either letter from 4

