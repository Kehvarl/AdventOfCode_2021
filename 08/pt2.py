from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
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

sum = 0
for line in content:
    mapping = {}
    letter_map = {}
    i, o = line.strip().split("|")
    input = i.split(" ")
    output = o.split(" ")

    for i in input:
        if len(i) in unique_segments:
            mapping[unique_segments[len(i)]] = set(list(i))

    for i in input:
        if len(i) == 6:
            # 6 9 0 6
            # 9     |4
            # 0     |1
            # 6     !1
            if mapping[4].issubset(set(list(i))):
                mapping[9] = set(list(i))
            elif mapping[1].issubset(set(list(i))):
                mapping[0] = set(list(i))
            elif not mapping[1].issubset(set(list(i))):
                mapping[6] = set(list(i))

    for i in input:
        if len(i) == 5:
            # 2 3 5 5
            # 2     !9
            # 3     |9
            # 5     |6
            if set(list(i)).issubset(mapping[6]):
                mapping[5] = set(list(i))
            elif set(list(i)).issubset(mapping[9]):
                mapping[3] = set(list(i))
            elif not set(list(i)).issubset(mapping[9]):
                mapping[2] = set(list(i))

    print(mapping)
    out = ""
    for o in output:
        so = set(list(o))
        for m in mapping:
            if so == mapping[m]:
                out += str(m)

    sum += int(out)
    print(out)

print(sum)

# 1     2
# 4     4
# 7     3
# 8     7
# 6 9 0 6
# 9     |4
# 0     |1
# 6     !1
# 2 3 5 5
# 2     !9
# 3     |1
# 5     |6

