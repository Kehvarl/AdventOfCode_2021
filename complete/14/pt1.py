from collections import defaultdict, Counter
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()

template = list(content[0].strip())
rules = []

for rule in content[2::]:
    pair, insert = rule.strip().split("->")
    rules.append((pair.strip(), insert.strip()))


def step(template):
    new_template = []
    for i in range(len(template) - 1):
        pair = template[i:i + 2]
        for rule, insert in rules:
            if pair == list(rule):
                new_template.append(template[i])
                new_template.append(insert)
                # new_template.append(template[i+1])
                break
    new_template.append(template[-1])

    return new_template

for r in range(10):
    template = step(template)
    print(len(template))

elements = set(template)
counts = defaultdict(int)
totals = Counter(template)
print(totals)
print(totals.most_common())
print(totals.most_common()[0][1] - totals.most_common()[-1][1])
