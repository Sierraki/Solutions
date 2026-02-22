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
    s=si()
    res=[]
    pin=0
    for i,j in enumerate(s):
        if j==s[pin]:
            continue
        else:
            res.append(i-pin )
            pin=i
    if pin!=n:
        res.append(n-pin)
    for i in res:
        if i>1 and s[0]!=s[-1]:
            print(len(res)+1)
            break
    else:
        print(len(res))

# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    size = ii()
    for _ in range(size):
        solve()
