from collections import defaultdict

with open("input.txt") as f:
    #content = f.readlines()
    lantern_fish = [int(x) for x in f.readlines()[0].strip().split(",")]

# track number of fish of each age
n = defaultdict(int)
for f in lantern_fish:
    n[f] += 1

# each day
# for each age, move all fish of that age to one age closer to spawning
# If the age is 0, start that number at both 6 and 8 to represent spawning
for day in range(256):
    f = defaultdict(int)
    for age, count in n.items():
        if age > 0:
            f[age - 1] += count
        else:
            f[6] += count
            f[8] += count
    n = f

print(sum(n.values()))
