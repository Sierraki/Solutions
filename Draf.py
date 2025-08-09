from collections import defaultdict, Counter
from math import sqrt, floor, gcd, lcm, prod
import bisect, re
from collections import deque
from typing import List, Optional
from fractions import Fraction


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        # 这是一个辅助方法，用于在调试时打印节点
        return f"TreeNode({self.val})"


def build_tree_from_list(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    # 检查空列表和空根节点
    if not nodes or nodes[0] is None:
        return None
    
    root = TreeNode(nodes[0])
    res=deque([root])
    pin=1
    
    while res and pin<len(nodes):
        cur=res.popleft()

        # 左节点
        if pin<len(nodes) and nodes[pin]!=None:
            cur.left=TreeNode(nodes[pin])
            res.append(cur.left)
        pin+=1

        # 右节点
        if pin < len(nodes) and nodes[pin] != None:
            cur.right = TreeNode(nodes[pin])
            res.append(cur.right)
        pin += 1
    return root
