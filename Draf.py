from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod
import bisect, re
from collections import deque
from typing import List


nums = [2, 3, 4, 5, 6]

l = r = 0
mx = 0
while l <= r and r < len(nums):
    arr = nums[l : r + 1]
    arr.sort()
    mx1 = arr[-1]
    if len(arr) <= 1:
        mx2 = mx1
    else:
        mx2 = arr[-2]

    if prod(arr) == gcd(mx1, mx2) * lcm(mx1, nums[0]):
        r += 1
    else:
        r += 1
        l += 1

    mx = max(mx, r - l)

print(mx)
