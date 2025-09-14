# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
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
            a = ""
            for j in i:
                a += str(j)
            ans += int(a)
        return ans
