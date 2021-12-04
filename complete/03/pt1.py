
file = "test.txt"
# file = "input.txt"


with open(file) as f:
    content = f.readlines()
    # content = [int(x) for x in f.readlines()]

ones = {}
count = {}

for line in content:
    line = [c for c in line.strip()]
    for i in range(len(line)):
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
        if i not in ones:
            ones[i] = int(line[i])
        else:
            ones[i] += int(line[i])

print(count)
print(ones)
gama = ""
epsilon = ""
for i in range(len(count)):
    if ones[i] > count[i]//2:
        gama += "1"
        epsilon += "0"
    else:
        gama += "0"
        epsilon += "1"

print(gama)
print(int(gama, 2))
print(epsilon)
print(int(epsilon, 2))

print(int(gama, 2) * int(epsilon, 2))