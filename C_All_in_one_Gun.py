from collections import defaultdict, Counter, deque
from math import sqrt, floor,gcd,ceil
from bisect import bisect, bisect_left
from itertools import accumulate as acc
from functools import cache, lru_cache
import heapq
import sys

input = sys.stdin.readline
def mii():
    return map(int, input().split())
def lmii():
    return list(map(int, input().split()))
def ii():
    return int(input())
def si():
    return input().strip()
def lacc(nums):
    return list(acc(nums))
def ms(numss):
    return "".join(map(str, numss))


def solve():
    n,h,k=mii()
    nums=lmii()

    total = sum(nums)
    cost = (h - 1) // total
    re = h - cost * total
    
    mi_prev = [0] * n
    mi_cur = float('inf')
    for i in range(n):
        if nums[i] < mi_cur:
            mi_cur = nums[i]
        mi_prev[i] = mi_cur
        
    mx_sf = [0] * n
    cur_mx = -float('inf')
    for i in range(n - 1, -1, -1):
        if nums[i] > cur_mx:
            cur_mx = nums[i]
        mx_sf[i] = cur_mx
        
    ans = 0
    for m in range(1, n + 1):
        ans += nums[m - 1]
        if m < n:
            res = max(ans, ans - mi_prev[m - 1] + mx_sf[m])
        else:
            res = ans
            
        if res >= re:
            print(cost * (n + k) + m)
            break
    pass

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
