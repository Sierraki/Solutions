# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def fun(root: TreeNode, res: list):
            if not root:
                return None
            if not root.left and not root.right:
                res.append(root.val)
            fun(root.left, res)
            fun(root.right, res)

        res1 = []
        res2 = []
        fun(root1, res1)
        fun(root2, res2)
        return res1 == res2
