from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect, bisect_left
from collections import deque
from typing import List, Optional
from fractions import Fraction

nums = [29, 25, 2, 12, 15, 42, 14, 6, 16, 9]
n = len(nums)
tar = 30

nums.sort()
print(nums)
lc = bisect(nums, tar) - 1
print(lc, nums[lc])

ans = n - lc
print(ans)
