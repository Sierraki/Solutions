from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque
from typing import List


nums = [7, 8, 3, 4, 15, 13, 4, 1]

nums.sort()
n = len(nums)
print(nums)
res = float('inf')

for _ in range(n // 2):
    ans = (nums[0] + nums[-1]) / 2
    del nums[0]
    nums.pop()
    res=min(res,ans)
print(res)
