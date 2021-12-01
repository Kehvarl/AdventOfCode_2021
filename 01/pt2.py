with open("input.txt") as f:
    content = f.readlines()

print(content)
depth = None
increase = 0

for i in range(len(content)-2):
    s = int(content[i]) + int(content[i+1]) + int(content[i+2])
    print(s)
    if depth is not None and s > depth:
        increase += 1
    depth = s

print(increase)
