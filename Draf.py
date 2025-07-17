from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


nums = [-6, -6, -6, -1]

ac = 0
cnt = 0
for i in range(len(nums) - 2, -1, -1):

    if nums[i] + ac != nums[i + 1]:
        cnt += 1
        nums[i] += ac
        gap = nums[i + 1] - nums[i]
        ac += gap
    nums[i] = nums[i + 1]

print(nums, cnt)
