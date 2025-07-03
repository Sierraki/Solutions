from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque

# items[0][0] 为容量，items[0][1]为价值
items = [[1, 50], [8, 10]]
capacity = 5
dp = [[0] * (capacity + 1) for _ in range(len(items))]
# 处理第一行
for i in range(len(dp[0])):
    if i >= items[0][0]:
        dp[0][i] = items[0][1]
    else:
        dp[0][i] = 0
for i in range(1, len(dp)):
    for j in range(capacity + 1):
        if j == 0:
            dp[i][j] = 0
        else:
            # 上一个，加上当前值还有空余再加上一个行的剩余容量最佳
            dp[i][j] =  dp[i - 1][j]
            # 选当前
            if j - items[i][0] >= 0:
                ans = items[i][1] + dp[i - 1][j - items[i][0]]
                dp[i][j] = max(dp[i][j], ans)
print(dp)
