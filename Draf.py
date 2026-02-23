import heapq
import sys
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt


nums = [1,1,1,1,1]
target = 3

n=len(nums)
res=[]
def dfs(start,path):
    if len(path)==n:
        res.append(path[:])
        return 
    for i in range(start,n):
        path.append(i*1)
        
