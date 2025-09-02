from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction

n = 12

dp = [0] * (n + 1)
mi = []
for i in range(1, n + 1):
    if i == floor(sqrt(i)) ** 2:
        dp[i] = 1
        mi.append(i)
    else:
        for j in mi:
            dif = i % (j)
            if dp[i] == 0:
                dp[i] = dp[j] * (i // (j)) + dp[i % (j)]
            else:
                dp[i] = min(dp[i], dp[j] * (i // (j)) + dp[i % (j)])
print([i for i in range(13)])
print(dp)
