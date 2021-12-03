
# file = "test.txt"
file = "input.txt"

with open(file) as f:
    content = f.readlines()
    # content = [int(x) for x in f.readlines()]


def more_ones(ones, position):
    count = 0
    for line in ones:
        line = [int(c) for c in line.strip()]
        count += line[position]
    return count >= len(ones)/2


def filter_ones(ones, position, value):
    return [ele for ele in ones if int(ele[position]) == value]


oxy_content = content.copy()
for pos in range(len(oxy_content[0])-1):
    val = 0
    if more_ones(oxy_content, pos):
        val = 1
    oxy_content = filter_ones(oxy_content, pos, val)

print(oxy_content)
print(int(oxy_content[0].strip(), 2))


co2_content = content.copy()
for pos in range(len(co2_content[0])-1):
    if(len(co2_content) == 1):
        break
    val = 0
    if not more_ones(co2_content, pos):
        val = 1
    co2_content = filter_ones(co2_content, pos, val)

print(co2_content)
print(int(co2_content[0].strip(), 2))

print(int(co2_content[0].strip(), 2) * int(oxy_content[0].strip(), 2))