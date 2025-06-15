from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque

nums = [84, 91, 18, 59, 27, 9, 81, 33, 17, 58]
cnt = defaultdict(list)
ans = -1
for i in nums:
    r = max([int(i) for i in str(i)])
    cnt[r].append(i)

res = [[i, sorted(j, reverse=True)] for i, j in cnt.items() if len(j) >= 2]

if res:
    for i, j in res:
        ans = max(j[0] + j[1], ans)
print(ans)
