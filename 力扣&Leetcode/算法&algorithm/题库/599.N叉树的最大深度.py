"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if not root:
            return 0
        else:
            ans = 0
            for i in root.children:
                ans = max(ans, self.maxDepth(i))
            return ans + 1
