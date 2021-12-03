

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]

pos = 0
depth = 0

for line in content:
    direction, amount = line.split()
    if direction == "up":
        depth -= int(amount)
    elif direction == "down":
        depth += int(amount)
    elif direction == "forward":
        pos += int(amount)

print(pos)
print(depth)
print(pos * depth)