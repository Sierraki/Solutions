from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List


nums = [4, 0, 5, -5, 3, 3, 0, -4, -5]
target = -2

nums.sort()
print(nums)


mi = float("inf")
res = float("inf")


for i in range(len(nums) - 2):
    # print(nums[i])
    l, r = i + 1, len(nums) - 1

    while l < r:
        ans = nums[i] + nums[l] + nums[r]

        if ans > target:
            if abs(ans - target) < mi:
                mi = abs(ans - target)
                res = ans
            r -= 1
        elif ans < target:
            if abs(ans - target) < mi:
                mi = abs(ans - target)
                res = ans
            l += 1
        else:
            res = ans
            break

print(res)
