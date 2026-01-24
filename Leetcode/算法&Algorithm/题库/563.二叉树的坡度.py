# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def fun(root):
            nonlocal ans
            if not root:
                return 0
            left = fun(root.left)
            right = fun(root.right)
            ans += abs(left - right)
            return root.val + left + right

        ans = 0
        fun(root)
        return ans


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def fun(root):
            if not root:
                return 0
            left = fun(root.left)
            right = fun(root.right)
            root.val += left + right
            return root.val

        def fun1(root):
            if not root:
                return
            left = root.left.val if root.left else 0
            right = root.right.val if root.right else 0
            root.val = abs(left - right)
            fun1(root.left)
            fun1(root.right)

        def fun3(root):
            nonlocal ans
            if not root:
                return 0
            ans += root.val
            fun3(root.left)
            fun3(root.right)

        ans = 0
        fun(root)
        fun1(root)
        fun3(root)
        return ans
