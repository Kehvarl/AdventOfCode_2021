from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    # content = [int(x) for x in f.readlines()]

links = defaultdict(list)

for line in content:
    source, dest = line.strip().split("-")
    links[source].append(dest)
    links[dest].append(source)


def search(edge, visited):
    if edge == 'end':
        return 1  # valid path
    if edge.islower() and edge in visited:
        return 0  # dead-end
    visited = visited.union({edge})
    count = 0
    for e in links[edge]:
        count += search(e, visited)
    return count


print(search('start', set()))
