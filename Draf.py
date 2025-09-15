from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod, ceil
from bisect import bisect, bisect_left
from collections import deque
from typing import List, Optional
from fractions import Fraction


coins = [10]
amount = 10


dp = [[0] * amount for _ in range(len(coins))]

cnt = {i: 0 for i in range(1, amount + 1)}

for i in range(len(coins)):
    for j in range((amount)):
        if i == 1:
            if coins[i] <= j + 1 and (j + 1) % coins[i] == 0:
                dp[i][j] = 1
        # 判断可否整除
        if (j + 1) % coins[i] == 0 and coins[i] >= j + 1:
            dp[i][j] += 1
        # 取上方

        dp[i][j] += dp[i - 1][j]

        if j + 1 - coins[i] >= 0 and j + 1 - coins[i] in cnt:
            dp[i][j] += cnt[j + 1 - coins[i]]

        cnt[j + 1] = max(cnt[j + 1], dp[i][j])
print(cnt)
print(dp)
print(dp[-1][-1])
