# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def fun(root):
            if not root:
                return None
            fun(root.left)
            res.append(root.val)
            fun(root.right)

        res = []
        fun(root)
        dummy = TreeNode(0)
        pin = dummy
        p = 0
        while p < len(res):
            pin.left = None
            pin.right = TreeNode(res[p])
            pin = pin.right
            p += 1
        return dummy.right
