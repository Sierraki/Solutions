# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal cnt
            if not root:
                return
            if root.val % 2 == 0:
                for i in [root.left, root.right]:
                    if i:
                        if i.left:
                            cnt += i.left.val
                        if i.right:
                            cnt += i.right.val
            dfs(root.left)
            dfs(root.right)

        cnt = 0
        dfs(root)
        return cnt
