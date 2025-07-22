from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List

nums = [1, 2, 3, 12]

ans = nums[0]

print(ans)
del nums[0]
print(nums)

mi = float("inf")
for idx, i in enumerate(nums):
    if i < mi:
        lc = idx
        mi = i
ans += mi
del nums[lc]
print(ans)
print(nums)

mi = float("inf")
for idx, i in enumerate(nums):
    if i < mi:
        lc = idx
        mi = i
ans += mi

print(ans)
print(nums)
