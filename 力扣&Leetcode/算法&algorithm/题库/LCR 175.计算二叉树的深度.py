# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculateDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            a = self.calculateDepth(root.left)
            b = self.calculateDepth(root.right)
            return max(a, b) + 1
