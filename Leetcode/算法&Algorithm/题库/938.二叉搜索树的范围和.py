# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def fun(root, ans):
            if not root:
                return None
            ans.append(root.val)
            fun(root.left, ans)
            fun(root.right, ans)

        ans = []
        fun(root, ans)
        return sum([i for i in ans if low < i < high]) + low + high
