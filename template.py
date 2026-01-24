from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
from itertools import accumulate as acc
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
def lacc(nums):
    return list(acc(nums))

size = ii()
for _ in range(size):
    n = ii()
    a, b = mii()
    nums = lmii()
