from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]


alu = []
for line in content:
    cmd = line.strip().split()
    alu.append(cmd)


def compute(alu, input):
    state = defaultdict(int)
    input = [int(x) for x in list(str(input))]
    i = 0

    for cmd in alu:
        if cmd[0] == 'inp':
            state[cmd[1]] += input[i]
            i += 1
        elif cmd[0] == 'add':
            a = state[cmd[1]]
            if cmd[2].isnumeric() or cmd[2][0] == '-':
                b = int(cmd[2])
            else:
                b = state[cmd[2]]
            state[cmd[1]] = a + b
        elif cmd[0] == 'mul':
            a = state[cmd[1]]
            if cmd[2].isnumeric() or cmd[2][0] == '-':
                b = int(cmd[2])
            else:
                b = state[cmd[2]]
            state[cmd[1]] = a * b
        elif cmd[0] == 'div':
            a = state[cmd[1]]
            if cmd[2].isnumeric() or cmd[2][0] == '-':
                b = int(cmd[2])
            else:
                b = state[cmd[2]]
            state[cmd[1]] = a // b
        elif cmd[0] == 'mod':
            a = state[cmd[1]]
            if cmd[2].isnumeric() or cmd[2][0] == '-':
                b = int(cmd[2])
            else:
                b = state[cmd[2]]
            state[cmd[1]] = a % b
        elif cmd[0] == 'eql':
            a = state[cmd[1]]
            if cmd[2].isnumeric() or cmd[2][0] == '-':
                b = int(cmd[2])
            else:
                b = state[cmd[2]]
            state[cmd[1]] = 1 if a == b else 0
    return state


sn = 98998519596997
while True:
    out = compute(alu, sn)
    if out['z'] == 0:
        print(sn, out)
        break
    sn -= 1
    while '0' in str(sn):
        sn -= 1
