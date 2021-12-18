from collections import defaultdict
from pprint import pprint

with open("test1.txt") as f:
    content = f.readlines()


def parse(s):
    def parse_helper(level=0):
        try:
            token = next(tokens)
        except StopIteration:
            if level:
                raise Exception('Missing close paren')
            else:
                return []
        if token == ']':
            if not level:
                raise Exception('Missing open paren')
            else:
                return []
        elif token == '[':
            return [parse_helper(level+1)] + parse_helper(level)
        elif token == ',':
            return parse_helper(level)
        else:
            return [int(token)] + parse_helper(level)
    tokens = iter(s)
    return parse_helper()


def explode(number, level=0):
    a, b = number
    if isinstance(a, list):
        a = explode(a, level + 1)
    if isinstance(b, list):
        b = explode(b, level + 1)
    return a, b


sf = parse("[[[[[9,8],1],2],3],4]")
print(explode(sf[0]))
