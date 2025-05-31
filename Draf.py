from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache

queries = [3, 1, 2, 1]
m = 5
print(queries)
nums = [i for i in range(1, m + 1)]
print(nums)
a = []
for i in queries:
    lc = nums.index(i)
    a.append(lc)
    tar = nums[lc]
    del nums[lc]
    nums.insert(0, tar)
    print(nums)
print(a)
