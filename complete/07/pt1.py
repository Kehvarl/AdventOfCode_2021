from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    #content = f.readlines()
    content = [int(x) for x in f.readlines()[0].strip().split(",")]

crabs = defaultdict(int)
for c in content:
    crabs[c] += 1

move_cost = defaultdict(int)
limit = max(crabs)

for c in crabs:
    dest = defaultdict(int)
    for d in crabs:
        move_cost[d] += abs(c - d) * crabs[c]

print(min(move_cost.values()))
