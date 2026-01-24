# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def fun(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [[root.val]]
            left = fun(root.left)
            right = fun(root.right)
            return [[root.val] + i for i in left + right]


        res = fun(root)
        ans = 0
        for i in res:
            ans = max(ans, max(i) - min(i))
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, mi, mx):
            nonlocal ans
            if not root:
                return 0
            ans = max(ans, abs(root.val - mx), abs(root.val - mi))
            mx1 = max(mx, root.val)
            mi1 = min(mi, root.val)
            dfs(root.left, mi1, mx1)
            dfs(root.right, mi1, mx1)

        ans = -float("inf")
        dfs(root, root.val, root.val)
        return ans
