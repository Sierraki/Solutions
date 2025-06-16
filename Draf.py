from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque

coins = [1, 2, 5]
amount = 11

if amount < 1:
    return 0
dp = [float("inf")] * (amount + 1)
dp[0] = 0
for i in range(1, amount + 1):
    for j in coins:
        if j <= i:
            dp[i] = min(dp[i], 1 + dp[i - j])
return -1 if dp[amount] == float("inf") else dp[amount]

