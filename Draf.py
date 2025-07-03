from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque

nums = [1, 2, 2, 3, 1, 4, 2]

cnt = defaultdict(list)
res = []
tar = max(Counter(nums).values())
for i, j in Counter(nums).items():
    if j == tar:
        res.append(i)

for idx, i in enumerate(nums):
    cnt[i].append(idx)

print(dict(cnt))
print(res)
mx = 0

for i in res:
    mx = max(mx, (cnt[i][-1] - cnt[i][0] + 1))
print(mx)
