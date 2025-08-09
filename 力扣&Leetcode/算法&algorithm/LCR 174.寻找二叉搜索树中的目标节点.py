# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTargetNode(self, root: Optional[TreeNode], cnt: int) -> int:
        # 中序遍历
        def fun(root):
            if not root:
                return
            fun(root.left)
            res.append(root.val)
            fun(root.right)

        res = []
        fun(root)
        return res[-cnt]
