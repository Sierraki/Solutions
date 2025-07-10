from collections import defaultdict, Counter
from math import sqrt, floor
import bisect, re
from functools import lru_cache
from collections import deque
from typing import List


s = "bbbab"

m = len(s)
dp = [[False] * m for _ in range(m)]
for i in range(m):
    for j in range(i + 1):
        if i >= j:
            if i == j:
                dp[j][i] = True
            else:
                if s[i] == s[j]:
                    if i - j <= 2:
                        dp[j][i] = True
                    else:
                        dp[j][i] = dp[j + 1][i - 1]
                else:
                    dp[j][i] = False
# 开头的最长
res1 = Counter()
# 结尾的最长
res2 = Counter()
res3 = []
mx=0
for i in range(m):
    for j in range(m):
        if dp[i][j]:
            res3.append([i, j])
            mx=max(mx,j-i+1)

for i, j in res3:
    res1[i] = max(res1[i], j - i + 1)

for i, j in res3:
    res2[j] = max(res2[j], j - i + 1)

for i in range(1,len(s)-1):
    a1=res2[i-1]+res1[i+1]
    
