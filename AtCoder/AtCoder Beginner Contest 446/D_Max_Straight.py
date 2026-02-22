import heapq
import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

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
    n=ii()
    nums=lmii()
    cnt=defaultdict(int)
    mx=1
    for i in nums:
        tar=i-1
        if tar not in cnt:
            cnt[i]=max(cnt[i],1)
        else:
            cnt[i]=max(cnt[i],cnt[tar]+1)
        mx=max(mx,cnt[i])
    print(mx)
# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
        solve()
