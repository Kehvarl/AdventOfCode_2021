from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]

opens = ['{', '[', '(', '<']
closes = ['}', ']', ')', '>']
valid = {'{': '}',
         '}': '{',
         '[': ']',
         ']': '[',
         '(': ')',
         ')': '(',
         '<': '>',
         '>': '<'}

bads = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

incompletes ={
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4}


scores = []

for line in content:
    score = 0
    open_queue = []
    is_valid = True
    text = list(line.strip())
    for i, t in enumerate(text):
        if t in opens:
            open_queue.append(t)
        elif t in closes:
            if t == valid[open_queue[-1]]:
                open_queue.pop(len(open_queue)-1)
            else:
                # print(i, t, open_queue[-1])
                is_valid = False
                break

    if len(open_queue) > 0 and is_valid:
        needed = []
        for char in open_queue:
            needed.append(valid[char])
        print(needed)
        for char in reversed(needed):
            score *= 5
            score += incompletes[char]
        print(score)
        scores.append(score)

scores.sort()
print(scores[len(scores)//2])

