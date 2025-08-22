"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return None
        res = deque([root])
        while res:
            n = len(res)
            for i in range(n):
                cur = res.popleft()
                if i < n - 1:
                    cur.next = res[0]
                if cur.left:
                    res.append(cur.left)
                if cur.right:
                    res.append(cur.right)
        return root
