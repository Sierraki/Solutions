from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


n = 4
k = 4

nums = [i for i in range(1, n + 1)]
res = deque(nums)
cnt = Counter(nums)
cnt[1] += 1

t = 0
cnt = Counter(nums)
print(cnt)
while max(cnt.values()) < 3:
    res.rotate(-t * k)
    cnt[res[0]] += 1
    print(res)
    t += 1
ans = [i for i, j in cnt.items() if j == 1]

print(ans)
