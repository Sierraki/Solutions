from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


events = [
    [7, 1],
    [19, 3],
    [9, 4],
    [12, 5],
    [2, 8],
    [15, 10],
    [18, 12],
    [7, 14],
    [19, 16],
]

cnt = Counter()

for idx, i in enumerate(events):
    if idx == 0:
        cnt[i[0]] += i[1]
    elif idx > 0:
        cnt[i[0]] += i[1] - events[idx - 1][1]
tar = max(cnt.values())
res = [i for i, j in cnt.items() if j == tar]
print(cnt)
