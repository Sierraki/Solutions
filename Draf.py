from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
from bisect import bisect, bisect_left
from itertools import accumulate
import heapq
import sys
import copy


def p(numss):
    for i in numss:
        print(i)


nums1 = [-3, -2]
nums2 = [1, 2]
k = 2

n = len(nums1)
m = len(nums2)
tmp = [[-float("inf")] * m for _ in range(n)]

dp = [[[-float("inf")] * m for _ in range(n)] for _ in range(k + 1)]
ans = -float("inf")
for i in range(n):
    for j in range(m):
        if i == j == 0:
            tmp[i][j] = nums1[i] * nums2[j]
        elif i == 0:
            tmp[i][j] = max(nums1[i] * nums2[j], tmp[i][j - 1])
        elif j == 0:
            tmp[i][j] = max(nums1[i] * nums2[j], tmp[i - 1][j])

        if i > 0 and j > 0:
            tmp[i][j] = max(
                nums1[i] * nums2[j], tmp[i - 1][j - 1], tmp[i - 1][j], tmp[i][j - 1]
            )
        ans=max(ans,tmp[i][j])


dp[1] = tmp
for i in range(2, len(dp)):
    # cur = dp[i]
    pre = dp[i - 1]
    for ii in range(i - 1, n):
        for jj in range(i - 1, m):
            # 当前值 cur_val
            cur_val = nums1[ii] * nums2[jj]
            # qianbiao左边上面
            res1 = cur_val + pre[ii - 1][jj - 1]
            # 跳过
            row = dp[i][ii - 1][jj] if ii > 0 else -float("inf")
            col = dp[i][ii][jj - 1] if jj > 0 else -float("inf")
            dp[i][ii][jj] = max(res1, row, col, dp[i][ii][jj])

            ans = max(ans, dp[i][ii][jj])
p(dp)

# p(tmp)
print(ans)
