from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque


matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]

m = len(matrix)
n = len(matrix[0])
dp = [[0] * n for _ in range(m)]

for i in range(m):
    if i == 0:
        dp[0] = matrix[0]
    else:
        for j in range(n):
            if j == 0:
                dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i - 1][j + 1])
            elif j == n - 1:
                dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1])
            else:
                dp[i][j] = matrix[i][j] + min(
                    dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1]
                )
print(dp)
