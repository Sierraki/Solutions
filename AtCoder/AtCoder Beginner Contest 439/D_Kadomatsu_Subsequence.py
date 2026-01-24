from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
import sys

input = sys.stdin.readline


def mii():
    return map(int, input().split())


def ii():
    return int(input())


n = ii()
nums = list(mii())
ans = 0
cnt = Counter()
total = Counter(nums)
for i in range(n):
    cur = nums[i]
    cnt[cur] += 1
    total[cur] -= 1
    if cur % 5 == 0:
        res1 = cur // 5 * 3
        res2 = cur // 5 * 7
        if res1 in cnt and res2 in cnt:
            ans += cnt[res1] * cnt[res2]
        if res1 in total and res2 in total:
            ans += total[res1] * total[res2]
print(ans)
