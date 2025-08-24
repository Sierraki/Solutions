# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def fun(root):
            if not root:
                return
            root.left, root.right = fun(root.right), fun(root.left)
            return root

        return fun(root)
