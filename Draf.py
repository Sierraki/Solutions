from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction


questions = [[21, 5], [92, 3], [74, 2], [39, 4], [58, 2], [5, 5], [49, 4], [65, 3]]

n = len(questions)
dp = [0] * n

for i in range(n - 1, -1, -1):
    dp[i] = max(questions[i][0], dp[i])
    if i + questions[i][1] + 1 < n:
        dp[i] = max(dp[i], questions[i][0] + dp[i + 1 + questions[i][1]])
    if i < n - 1:
        dp[i] = max(dp[i], dp[i + 1])

print(dp)
