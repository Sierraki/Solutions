# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def fun(root):
            if not root:
                return None
            fun(root.left)
            fun(root.right)
            res.add(root.val)

        res = set()
        fun(root)
        return len(res) == 1
