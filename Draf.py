

from operator import le
from turtle import up


nums1 = ["sumRange", "update", "sumRange"]
aws = [[0, 2], [1, 2], [0, 2]]

nums = [1, 3, 5]
n = len(nums)
tree = [0] * 4 * n

def build(node, left, right):
    if left == right:
        tree[node] = nums[left]
        return
    mid = (left + right) // 2
    left_node = node * 2 + 1
    right_node = left_node + 1
    build(left_node, left, mid)
    build(right_node, mid + 1, right)
    tree[node] = tree[left_node] + tree[right_node]


def _update(node, idx, val, left, right):
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
        _update(left_node, idx, val, left, mid)
    else:
        # 目标在右半区，只去右边找！
        _update(right_node, idx, val, mid + 1, right)

    # 3. 回溯：儿子们改完后，更新老爸的值
    tree[node] = tree[left_node] + tree[right_node]

def update(index, val):
    
    return _update(0,index,val,0,n-1)


def _query(node, L, R, left, right):
    # 1. 完美包围：当前区间 [left, right] 完全在目标 [L, R] 内部
    if L <= left and right <= R:
        return tree[node]  # 直接返回现成的和，不往下查了
    mid = (left + right) // 2
    left_node = 2 * node + 1
    right_node = 2 * node + 2
    res = 0  # 用来攒积木的篮子

    # 2. 左半区有我们需要的数据吗？
    if L <= mid:
        res += _query(left_node, L, R, left, mid)

    # 3. 右半区有我们需要的数据吗？
    if R > mid:
        res += _query(right_node, L, R, mid + 1, right)

    # 4. 把左右要到的数据拼起来返回
    return res


def sumRange(left, right):
    return _query(0,left,right,0,n-1)

build(0, 0, n - 1)
for i, j in enumerate(nums1):
    if j == "sumRange":
        a, b = aws[i]
        sumRange(a, b)
    if j == "update":
        a, b = aws[i]
        update(a, b)

print(tree)
