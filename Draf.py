from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque
from typing import List


text1 = "abcde"
text2 = "ace"
m = len(text1)
n = len(text2)
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if text1[j - 1] == text2[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
print(dp)
