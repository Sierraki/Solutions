from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re

word = "abcdeafdef"

cnt = defaultdict(list)
for idx, i in enumerate(word):
    cnt[i].append(idx)

print(dict(cnt))

nums = [
    (2, 7),
    (2, 8),
    (2, 16),
    (2, 17),
    (3, 9),
    (3, 19),
    (3, 21),
    (4, 10),
    (4, 11),
    (4, 13),
    (4, 15),
    (4, 20),
    (5, 9),
    (5, 19),
    (5, 21),
    (6, 10),
    (6, 11),
    (6, 13),
    (6, 15),
    (6, 20),
    (7, 16),
    (7, 17),
    (8, 16),
    (8, 17),
    (9, 19),
    (9, 21),
    (10, 13),
    (10, 15),
    (10, 20),
    (11, 15),(15, 20),
    (11, 20),
    (12, 18),
    (13, 20),
    (14, 18),
    
]
nums.sort(key=lambda x: x[1])

cnt = 0
le = -1

for start, end in nums:
    if start > le:
        cnt += 1
        le = end

print(cnt)
