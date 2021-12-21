import random
from collections import defaultdict
from pprint import pprint

Memo = {}


def count_win(p1, p2, s1, s2):
    if s1 >= 21:
        return 1, 0
    if s2 >= 21:
        return 0, 1
    if (p1, p2, s1, s2) in Memo:
        return Memo[(p1, p2, s1, s2)]

    win_counts = (0, 0)
    for d1 in range(1, 4):
        for d2 in range(1, 4):
            for d3 in range(1, 4):
                new_p1 = (p1 + d1 + d2 + d3) % 10
                new_s1 = s1 + new_p1 + 1

                x1, y1 = count_win(p2, new_p1, s2, new_s1)
                win_counts = (win_counts[0] + y1, win_counts[1] + x1)
    Memo[(p1, p2, s1, s2)] = win_counts
    return win_counts


print(max(count_win((8-1), (3-1), 0, 0)))
