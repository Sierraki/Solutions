# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def fun(root):
            if not root:
                return
            res.add(root.val)
            fun(root.left)
            fun(root.right)

        res = set()
        fun(root)
        ans = sorted(list(res))
        if len(ans) < 2:
            return -1
        return ans[1]
