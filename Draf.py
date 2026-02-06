from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
from bisect import bisect, bisect_left
from itertools import accumulate
import heapq

def p(numss):
    for i in numss:
        print(i)


def fun(X,Y,total,ai):
    return (total-X*ai)//(Y-X)

