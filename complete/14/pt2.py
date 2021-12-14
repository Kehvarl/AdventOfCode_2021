from collections import defaultdict, Counter
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()

template = content[0].strip()
rules = {}

for rule in content[2::]:
    pair, insert = rule.strip().split("->")
    rules[pair.strip()] = insert.strip()

pairs = defaultdict(int)
for i in range(len(template) - 1):
    pair = template[i:i + 2]
    pairs[pair] += 1


def step(pairs):
    new_pairs = defaultdict(int)
    for pair, cnt in pairs.items():
        insert = rules[pair]
        new_pairs[pair[0] + insert] += cnt
        new_pairs[insert + pair[1]] += cnt

    return new_pairs


for r in range(40):
    pairs = step(pairs)

totals = Counter()
for pair, cnt in pairs.items():
    totals[pair[0]] += cnt
    totals[pair[1]] += cnt
totals[template[0]] += 1
totals[template[-1]] += 1
totals = Counter({elem: cnt // 2 for elem, cnt in totals.items()})
print(totals)
print(totals.most_common())
print(totals.most_common()[0][1] - totals.most_common()[-1][1])
