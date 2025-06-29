from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque


cost = [10, 15, 20]
cost.append(0)
dp = [0] * len(cost)


for i in range(2, len(cost)):
    dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])


print(cost)
print(dp)
