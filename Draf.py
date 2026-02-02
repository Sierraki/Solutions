from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
from itertools import accumulate as acc

import heapq
import copy
import sys

# import __hello__
# import this

input = sys.stdin.readline


def p(nums):
    for i in nums:
        print(i)


def lacc(nums):
    return list(acc(nums))


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
