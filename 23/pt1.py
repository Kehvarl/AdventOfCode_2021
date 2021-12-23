from collections import defaultdict
from pprint import pprint


# A 1
# B 10
# C 100
# D 1000

# Corridor Length 11
# Rooms
# A 3
# B 5
# C 7
# D  9

test_rooms = [['B', 'A'],
              ['C', 'D'],
              ['B', 'C'],
              ['D', 'A']]

real_rooms = [['B', 'D'],
              ['A', 'C'],
              ['A', 'B'],
              ['D', 'C']]

corridor = ["" for c in range(11)]

costs = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000}

targets = {
    'A': 3,
    'B': 5,
    'C': 7,
    'D': 9}

