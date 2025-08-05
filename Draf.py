from collections import defaultdict, Counter
from math import sqrt, floor,gcd
import bisect, re
from collections import deque
from typing import List

nums = [-1, 1, 2, 3, 1]
target = 2

nums.sort()
ans = 0
l, r = 0, len(nums) - 1

while l < r:
    if nums[l] + nums[r] >= target:
        r -= 1
    else:
        ans += r - 1
        l += 1
print(nums)
print(ans)
