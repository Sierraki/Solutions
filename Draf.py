from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque

words = ["kuvp", "q"]
order = "ngxlkthsjuoqcpavbfdermiywz"

cnt = Counter()
for idx, i in enumerate(order):
    cnt[i] += idx

res = []
for i in words:
    ans = 0
    for j in i:
        ans += cnt[j]
    if len(res) > 0:
        if ans <= res[-1]:
            print(False)
    res.append(ans)
print(True)

print(res)
