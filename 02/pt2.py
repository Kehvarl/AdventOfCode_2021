

with open("test.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]

pos = 0
aim= 0
depth = 0

for line in content:
    direction, amount = line.split()
    if direction == "up":
        aim -= int(amount)
    elif direction == "down":
        aim += int(amount)
    elif direction == "forward":
        pos += int(amount)
        depth += aim*int(amount)

print(pos)
print(depth)
print(pos * depth)