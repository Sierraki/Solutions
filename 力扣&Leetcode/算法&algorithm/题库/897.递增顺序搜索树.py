# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def fun(root):
            if not root:
                return None
            res.append(root.val)
            fun(root.left)
            fun(root.right)

        res = []
        fun(root)
        res.sort()
        root = TreeNode(res[0])
        pin = root
        for i in res[1:]:
            cur = TreeNode(i)
            pin.right = cur
            pin.left = None
            pin = pin.right
        return root
