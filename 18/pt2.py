import math
from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()

DIGITS = '0123456789'


def try_explode(num):
    num_str = str(num).replace(' ', '')
    depth = 0
    for idx, c in enumerate(num_str):
        if c == '[':
            depth += 1
            if depth == 5:
                # Explode!
                end_idx = num_str.find(']', idx)
                a, b = list(map(int, num_str[idx+1:end_idx].split(',')))
                left = num_str[:idx]
                for lidx in range(len(left)-1, -1, -1):
                    c = left[lidx]
                    if c in DIGITS:
                        term = max(i for i in range(lidx)
                                   if left[i] not in DIGITS)
                        val = int(left[term+1:lidx+1])
                        val += a
                        left = left[:term+1] + str(val) + left[lidx+1:]
                        break
                mid = '0'
                right = num_str[end_idx+1:]
                for ridx, c in enumerate(right):
                    if c in DIGITS:
                        term = min(i for i in range(ridx+1, len(right))
                                   if right[i] not in DIGITS)
                        val = int(right[ridx:term])
                        val += b
                        right = right[:ridx] + str(val) + right[term:]
                        break
                return eval(left + mid + right)
        elif c == ']':
            depth -= 1
    return None


def split(number):
    if isinstance(number, list):
        a, b = number
        a1 = split(a)
        if a1 is not None:
            return [a1, b]
        b1 = split(b)
        if b1 is not None:
            return [a, b1]
        return None
    if number > 9:
        a = math.floor(number/2)
        b = math.ceil(number/2)
        return [a, b]
    return None


def reduce(number):
    while True:
        test = try_explode(number)
        if test is not None:
            number = test
            continue

        test = split(number)
        if test is not None:
            number = test
            continue
        return number


def magnitude(x):
    if isinstance(x, int):
        return x
    return 3 * magnitude(x[0]) + 2 * magnitude(x[1])


nums = []
for line in content:
    num = eval(line)
    nums.append(num)

fish_nums = defaultdict(list)
maxfish = 0
for n1 in nums:
    for n2 in nums:
        if n1 != n2:
            test = magnitude(reduce([n1, n2]))
            maxfish = max(maxfish, test)

print(maxfish)
