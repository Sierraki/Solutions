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
