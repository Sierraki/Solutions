from collections import defaultdict, Counter
import bisect
from typing import List
from math import sqrt, floor


nums = [1, 2, 3, 3, 2, 2]

target = max(nums)

mx = cur = 0
left = right = 0

while right < len(nums):
    if nums[right] == nums[left] == target:
        right += 1
        cur += 1
        mx = max(cur, mx)
    else:
        right += 1
        left = right
        cur = 0
print(mx)
