from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache

nums = [0, 1, 1]

res = [False] * len(nums)
print(res)
a = []
for i in range(len(nums)):
    a += str(nums[i])
    ans = int("".join(list(a)), 2)
    if ans % 5 == 0:
        res[i] = True
print(res)
