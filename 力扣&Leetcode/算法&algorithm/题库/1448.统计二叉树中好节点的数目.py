# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(root, mx):
            nonlocal cnt
            if not root:
                return 0
            if root.val >= mx:
                cnt += 1
            mx = max(root.val, mx)
            dfs(root.left, mx)
            dfs(root.right, mx)

        cnt = 0
        dfs(root, root.val)
        return cnt
