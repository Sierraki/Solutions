from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction

nums1 = [13, 4, 2, 4]
nums2 = [11, 14, 8, 13]

n = len(nums1)
res = [0] * n

for i in range(n):
    if i == 0:
        res[0] = min(nums1[0], nums2[0])
    else:
        if nums1[i] >= res[i - 1] and nums2[i] >= res[i - 1]:
            res[i] = min(nums1[i], nums2[i])
        else:
            if nums1[i] >= res[i - 1]:
                res[i] = nums1[i]
            elif nums2[i] >= res[i - 1]:
                res[i] = nums2[i]
            else:
                res[i] = min(nums1[i], nums2[i])
print(res)


def fun(res: list) -> int:
    dp = [0] * n
    dp[0] = 1
    ans = 1
    for i in range(1, n):
        if res[i] >= res[i - 1]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 1
        ans = max(ans, dp[i])
    return ans


print(fun(res), fun(nums1), fun(nums2))
