from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction

n = 10
x = 2

res = [i**x for i in range(1, n + 1) if i**x <= n]

dp = [[0] * (n + 1) for _ in range(len(res))]

for i in range(len(dp)):
    for j in range(len(dp[0])):
        if i == 0:
            if res[i] <= j:
                dp[i][j] = 1
        else:
            if res[i] <= j:
                dp[i][j] = res[i]
            if j - res[i] > 0:
                dp[i][j] += dp[i - 1][j - res[i]]

print(res)
print(dp)
