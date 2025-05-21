from collections import defaultdict, Counter
import bisect
from typing import List
from math import sqrt, floor


nums = [1, 2, -1, -2, 1, 0, -1]

nums = list(set(nums))
nums.sort(reverse=True)

cur = nums[0]
print(nums,cur)
for i in range(1, len(nums)):
    last = cur
    cur += nums[i]
    if cur <= last:

        break

print(last)
