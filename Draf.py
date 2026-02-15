from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
from bisect import bisect, bisect_left
from itertools import accumulate
from functools import cache, lru_cache
import heapq
import copy


def p(numss):
    for i in numss:
        print(i)

nums = [1, 3, 5, 7, 9, 11, 13]

n = len(nums)

tree = [0] * (n * 4)


def build(node, left, right):
    if left == right:
        tree[node] = nums[left]
        return node
    mid = (left + right) // 2
    left_node = 2 * node + 1
    right_node = 2 * node + 2
    build(left_node, left, mid)
    build(right_node, mid + 1, right)
    tree[node] = tree[left_node] + tree[right_node]


build(0, 0, n - 1)

print("建好的树:", tree)
