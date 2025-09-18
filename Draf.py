from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect, bisect_left
from collections import deque
from typing import List, Optional
from fractions import Fraction

nums = [1, 3, 5, 2, 1, 3, 1]

nums.sort(reverse=True)
res = nums.copy()
res.sort()
nums = deque(nums)
res = deque(res)
cnt = 0

while nums:
    if res[-1] > nums[0]:
        cnt += 1
        res.pop()
        nums.popleft()
    else:
        nums.popleft()

print(res, nums, cnt)
