

with open("input.txt") as f:
    #content = f.readlines()
    lantern_fish = [int(x) for x in f.readlines()[0].strip().split(",")]

for day in range(80):
    for f in range(len(lantern_fish)):
        fish = lantern_fish[f]
        fish -= 1
        if fish < 0:
            fish = 6
            lantern_fish.append(8)
        lantern_fish[f] = fish
    print(lantern_fish)

print(len(lantern_fish))