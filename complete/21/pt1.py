import random
from collections import defaultdict
from pprint import pprint

player_1 = 8 # 4
score_1 = 0
player_2 = 3 # 8
score_2 = 0

def next_roll(r):
    r += 1
    if r == 101:
        r = 1
    return r

def take_turn(player, start):
    # roll = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    start = next_roll(start)
    roll = start
    start = next_roll(start)
    roll += start
    start = next_roll(start)
    roll += start

    player = player + roll
    while player > 10:
        player -= 10
    return player, start


turn = 0
start = 0
rolls = 0
while True:
    turn += 1
    player_1, start = take_turn(player_1, start)
    score_1 += player_1
    rolls += 3
    if score_1 >= 1000:
        break
    player_2, start = take_turn(player_2, start)
    score_2 += player_2
    rolls += 3
    if score_2 >= 1000:
        break

print(turn, rolls, player_1, score_1, player_2, score_2)
print(min(score_1, score_2) * rolls)