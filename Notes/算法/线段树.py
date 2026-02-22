import copy
import heapq
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from itertools import accumulate
from math import ceil, floor, gcd, sqrt


def p(numss):
    for i in numss:
        print(i)


nums = [3, 1, 4, 1, 5, 9, 2]
n = len(nums)

tree = [0] * 4 * n

def build(node, left, right):
    if left == right:
        tree[node] = nums[left]
        return
    mid = (left + right) // 2
    left_node = 2 * node + 1
    right_node = 2 * node + 2
    build(left_node, left, mid)
    build(right_node, mid + 1, right)
    tree[node] = tree[left_node] + tree[right_node]

# node: 当前的房间号
# idx: 我们要修改的目标在 nums 里的下标
# cur: 我们要修改成的新值
# left, right: 当前 node 管辖的范围
def update(node, idx, val, left, right):
    # 1. 找到了那个唯一的叶子节点！
    if left == right:
        tree[node] = val
        # nums[idx] = val  # 可选：如果你也想让原数组保持同步的话可以加上
        return
    mid = (left + right) // 2
    left_node = 2 * node + 1
    right_node = 2 * node + 2

    # 2. 核心导航逻辑：目标 idx 到底在左边还是右边？
    if idx <= mid:
        # 目标在左半区，只去左边找！
        update(left_node, idx, val, left, mid)
    else:
        # 目标在右半区，只去右边找！
        update(right_node, idx, val, mid + 1, right)

    # 3. 回溯：儿子们改完后，更新老爸的值
    tree[node] = tree[left_node] + tree[right_node]

def query(node, L, R, left, right):
    # 1. 完美包围：当前区间 [left, right] 完全在目标 [L, R] 内部
    if L <= left and right <= R:
        return tree[node]  # 直接返回现成的和，不往下查了
    mid = (left + right) // 2
    left_node = 2 * node + 1
    right_node = 2 * node + 2
    res = 0  # 用来攒积木的篮子

    # 2. 左半区有我们需要的数据吗？
    if L <= mid:
        res += query(left_node, L, R, left, mid)

    # 3. 右半区有我们需要的数据吗？
    if R > mid:
        res += query(right_node, L, R, mid + 1, right)

    # 4. 把左右要到的数据拼起来返回
    return res


build(0, 0, n - 1)
print(tree)
update(0, 1, 10, 0, n - 1)
print(tree)
cur1 = query(0, 0, 1 + 1, 0, n - 1)
print(cur1)
