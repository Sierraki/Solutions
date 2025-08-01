from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


nums = [9, 5, 7, 8, 7, 9, 8, 2, 0, 7]

cnt = Counter()

nums.sort()
print(nums)
l, r = 0, len(nums) - 1

while l < r:
    ans = (nums[l] + nums[r]) // 2
    cnt[ans] += 1
    l += 1
    r -= 1
print(len(cnt))
print(cnt)
