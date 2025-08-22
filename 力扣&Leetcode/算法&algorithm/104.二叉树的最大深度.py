# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            ans = 0
            for i in [root.left, root.right]:
                ans = max(ans, self.maxDepth(i))
            return ans + 1


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            a = self.maxDepth(root.left)
            b = self.maxDepth(root.right)
            return max(a, b) + 1
