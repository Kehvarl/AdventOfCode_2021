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

score = 0

for line in content:
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
                print(i, t, open_queue[-1])
                score += bads[t]
                break

print(score)

