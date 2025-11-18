# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def fun(root: TreeNode) -> list[int]:
            if not root:
                return
            fun(root.left)
            res.append(root.val)
            fun(root.right)

        res = []
        fun(root)
        for i in range(1, len(res)):
            if res[i - 1] >= res[i]:
                return False
        return True
