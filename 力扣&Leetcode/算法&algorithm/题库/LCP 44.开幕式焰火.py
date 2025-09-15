# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def numColor(self, root: TreeNode) -> int:
        res = set()
        ans = deque([root])
        while ans:
            cur = ans.popleft()
            res.add(cur.val)
            if cur.left:
                ans.append(cur.left)
            if cur.right:
                ans.append(cur.right)
        return len(res)
