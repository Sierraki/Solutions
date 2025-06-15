from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque

nums = [8, 4, 2, 8, 4]

mod = 10**9 + 7

cl = Counter()
cr = Counter(nums)
cr[nums[0]] -= 1
n = len(nums)
ans = 0

for i in range(1, n - 1):
    cl[nums[i - 1]] += 1
    cr[nums[i]] -= 1
    tar = nums[i] * 2
    res = cl[tar] * cr[tar]
    ans = (ans + res) % mod
print(ans)
