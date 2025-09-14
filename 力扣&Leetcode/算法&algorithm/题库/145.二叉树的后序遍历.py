# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def fun(root: TreeNode) -> list[int]:
            if not root:
                return
            fun(root.left)
            fun(root.right)
            res.append(root.val)

        res = []
        fun(root)
        return res
