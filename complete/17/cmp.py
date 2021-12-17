with open("compare.txt") as f:
    content = f.readline().strip()
pairs = content.split(' ')
valid = set()
count = 0
for p in pairs:
    count += 1
    if p == '':
        continue
    a, b = p.split(',')
    valid.add((int(a), int(b)))

