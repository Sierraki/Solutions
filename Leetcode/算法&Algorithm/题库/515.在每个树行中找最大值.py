# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        cur = deque([root])
        while cur:
            size = len(cur)
            a = []
            for _ in range(size):
                aa = cur.popleft()
                a.append(aa.val)
                if aa.left:
                    cur.append(aa.left)
                if aa.right:
                    cur.append(aa.right)
            res.append(a)
        return [max(i) for i in res]
