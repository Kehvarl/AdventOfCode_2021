from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    #content = f.readlines()
    content = [int(x,16) for x in f.readline().strip()]

bits = ""
for c in content:
 bits += format(c, "04b")

print(bits)

# VVVTTTAAAAABBBBBCCCCC

versions = []
values = []

def parse(bits, pos=0):
    global versions
    global values
    version = bits[pos:pos+3]
    versions.append(version)
    pos += 3
    type = bits[pos:pos+3]
    pos += 3
    if type == '100':
        readbits = True
        while readbits:
            v = bits[pos:pos+5]
            print(v)
            pos += 5
            check = v[0]
            v = v[1:]
            if check == '0':
                readbits = False
            values.append(v)
    else:
        i = bits[pos]
        pos += 1
        print(i)
        if i == '0':
            l = bits[pos:pos+15]
            pos += 15
            print(l, pos+int(l, 2))
            limit = pos + int(l, 2)
            while pos < limit:
                pos = parse(bits, pos)
        else:
            l = bits[pos:pos+11]
            pos += 11
            print(l, int(l, 2))
            for p in range(int(l, 2)):
                pos = parse(bits, pos)

    return pos

parse(bits)
print(versions, values)
s = [int(x, 2) for x in versions]

print(sum(s))