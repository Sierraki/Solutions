import heapq
import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

input = sys.stdin.readline


# num
def ii():
    return int(input())
def mii():
    return map(int, input().split())
def lmii():
    return list(map(int, input().split()))
# string
def lmsi():
    return list(map(str, si()))
def si():
    return input().strip()
def ms(numss):
    return "".join(map(str, numss))
# else
def lacc(nums):
    return list(acc(nums))
def matt(row, col):
    return [[0] * col for _ in range(row)]



def solve():
    n = ii()
    nums = lmii()

    if n < 4:
        print(0)
        return
    ans = []
    for i in range(1, n):
        if nums[i - 1] < nums[i]:
            ans += ['+']
        elif nums[i - 1] > nums[i]:
            ans += ['-']
        else:
            ans += ['x']
    cur = ans[0]
    cnt = 0
    res = []
    for i, j in enumerate(ans):
        if j == cur:
            cnt += 1
        else:
            res.append([cur, cnt])
            cur = j
            cnt = 1
    if cnt > 0:
        res.append([cur, cnt])
    anss = 0
    for i in range(len(res) - 2):
        a, b, c = res[i:i + 3]
        if a[0] == c[0] == '+' and b[0] == '-':
            anss += a[1] * c[1]
    print(anss)
    pass

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
