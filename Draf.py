from collections import defaultdict, Counter
import bisect
from typing import List
from math import sqrt, floor


players = [1, 100]
trainers = [100, 1]
players.sort()
print(players)
trainers.sort()
cnt = 0

for i in trainers:
    if players == []:
        break
    lc = bisect.bisect_left(players, i)
    # print(i, lc)
    if lc - 1 >= 0 and players[lc - 1] <= i:
        cnt += 1
        del players[lc - 1]
    elif lc < len(players) and players[lc] <= i:
        cnt += 1
        del players[lc]

print(cnt)
