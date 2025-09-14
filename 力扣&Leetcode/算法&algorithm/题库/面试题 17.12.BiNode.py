# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBiNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def fun(root):
            if not root:
                return
            res.append(root.val)
            fun(root.left)
            fun(root.right)

        res = []
        fun(root)
        res.sort()
        head = root
        pin = 0
        while pin < len(res):
            head.val = res[pin]
            head.left = None
            pin += 1
            if pin < len(res):
                head.right = TreeNode()
                head = head.right
        return root
