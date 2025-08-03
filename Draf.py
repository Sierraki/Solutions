from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from collections import deque
from typing import List

n = 5


dp = [0] * (n + 1)

dp[0] = 1
dp[1] = 1
dp[2] = 2


for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

print(dp)
