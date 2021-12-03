with open("input.txt") as f:
    content = f.readlines()

print(content)
depth = int(content[0])
increase = 0

for v1 in content:
    if int(v1) > depth:
        increase += 1
    depth = int(v1)

print(increase)
