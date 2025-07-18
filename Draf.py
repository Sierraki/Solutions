from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List

nums = [1, 3, 2, 1, 5, 4]
k = 2


ans = 0

for idx, i in enumerate(nums):
    a = idx - k
    b = idx + k
    if 0 <= a <= b <= len(nums) - 1:
        if i > nums[a] and i > nums[b]:
            ans += i
    else:
        if 0 <= a <= len(nums) - 1:
            if i > nums[a]:
                ans += i
        elif 0 <= b <= len(nums) - 1:
            if i > nums[b]:
                ans += i
print(ans)
