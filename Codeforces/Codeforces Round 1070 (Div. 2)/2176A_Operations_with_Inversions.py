from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
from itertools import accumulate
import sys

input = sys.stdin.readline
def mii():
    return map(int, input().split())
def lmii():
    return list(map(int, input().split()))
def ii():
    return int(input())
def si():
    return input()[:-1]


size = ii()
for _ in range(size):
    n = ii()
    nums = lmii()
    mx=-float('inf')
    ans=0
    for i in range(n):
        mx=max(mx,nums[i])
        if nums[i]<mx:
            ans+=1
    print(ans)