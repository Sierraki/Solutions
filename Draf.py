from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect, bisect_left
from collections import deque
from typing import List, Optional
from fractions import Fraction
import pandas as pd

nums = [1, 0, 1]
firstLen = 1
secondLen = 1
s = 0
prefix = []
for i in nums:
    s += i
    prefix.append(s)


print(prefix)
top = (
    [0] * (firstLen - 1)
    + [prefix[firstLen - 1]]
    + [prefix[i] - prefix[i - firstLen] for i in range(firstLen, len(prefix))]
)
down = (
    [0] * (secondLen - 1)
    + [prefix[secondLen - 1]]
    + [prefix[i] - prefix[i - secondLen] for i in range(secondLen, len(prefix))]
)

print(top)
print(down)
dp = [[0] * (len(nums)) for _ in range(len(nums))]
ans = 0
for i in range(len(dp)):
    for j in range(len(dp[0])):
        if (0 <= i - secondLen + 1 <= i <= j - firstLen + 1 <= j < len(nums)) or (
            0 <= j - firstLen + 1 <= j <= i - secondLen + 1 <= i < len(nums)
        ):
            dp[i][j] = top[j] + down[i]
            ans = max(ans, dp[i][j])
print(dp)
print(ans)
