

with open("input.txt") as f:
    content = f.readlines()

for v1 in content:
    for v2 in content:
        if int(v1) + int(v2) == 2020:
            print(v1, v2, (int(v1)*int(v2)))
