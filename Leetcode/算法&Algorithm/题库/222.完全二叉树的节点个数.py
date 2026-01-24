# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def fun(root=TreeNode) -> List:
            if not root:
                return None
            res.append(root.val)
            fun(root.left)
            fun(root.right)

        res = []
        fun(root)
        return len(res)
