from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod
import bisect, re
from collections import deque
from typing import List
from fractions import Fraction


nums = [2, 5, 3, 5]
target = 10 - 4

nums.sort()
l, r = 0, len(nums) - 1
ans = 0
while l < r:
    if nums[l] + nums[r] <= target:
        ans += r - l
        l += 1
    else:
        r -= 1

print(ans)
