# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def fun(root):
            if not root:
                return
            fun(root.left)
            res.append(root.val)
            fun(root.right)

        res = []
        fun(root)
        return (res) == sorted(list(set(res)))
