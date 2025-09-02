"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []
        res = deque([root])
        ans = []
        while res:
            n = len(res)
            a = []
            for i in range(n):
                cur = res.popleft()
                a.append(cur.val)
                for j in cur.children:
                    res.append(j)
            ans.append(a)
        return ans
