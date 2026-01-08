# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def fun(root):
            if not root:
                return 0
            left = fun(root.left)
            right = fun(root.right)
            root.val += left + right
            return root.val

        fun(root)
        total = root.val
        mx = -float("inf")

        def fun(root):
            nonlocal mx
            if not root:
                return 0
            mx = max(mx, root.val * (total - root.val))
            fun(root.left)
            fun(root.right)
            return

        fun(root)
        return mx % (10**9 + 7)
