import heapq
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate as acc
from math import ceil, floor, gcd, sqrt

k = 3

res = []
swap = [True]

tar = ["01", "10"]

def dfs(cur): 
    if len(cur) == k:
        if cur not in tar:
            return cur
    res1= dfs(cur + '1') 
    if res1 :
        return res1
    res2= dfs(cur + '2') 
    if res2 :
        return res2
    
print(dfs(''))
