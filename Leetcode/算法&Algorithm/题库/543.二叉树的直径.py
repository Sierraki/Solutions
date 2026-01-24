# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def fun(root):
            nonlocal res
            if not root:
                return 0
            left = fun(root.left)
            right = fun(root.right)
            cur = left + right
            res = max(res, cur)
            return 1 + max(left, right)

        res = 0
        fun(root)
        return res
