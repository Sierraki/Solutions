# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        def fun(root):
            if not root:
                return
            res.append(root.val)
            fun(root.left)
            fun(root.right)

        res = []
        fun(root)
        pin = 1
        head = root
        root.left = None
        while head:
            head.left = None
            if pin < len(res):
                head.right = TreeNode(res[pin])
            else:
                break
            pin += 1
            head = head.right
