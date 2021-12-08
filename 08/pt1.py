from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]

segments = {
    2: [1],
    3: [7],
    4: [4],
    # 5: [2, 3, 5],
    # 6: [6, 9, 0],
    7: [8]
}

counts = defaultdict(int)
sum = 0

for line in content:
    i, o = line.strip().split("|")
    input = i.split(" ")
    output = o.split(" ")

    for o in output:
        if len(o) in segments:
            counts[segments[len(o)][0]] += 1
            sum += 1
print(counts, sum)
