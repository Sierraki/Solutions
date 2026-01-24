# 自下向上
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            ans = 0
            for i in [root.left, root.right]:
                ans = max(ans, self.maxDepth(i))
            return ans + 1

# 自下向上
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            a = self.maxDepth(root.left)
            b = self.maxDepth(root.right)
            return max(a, b) + 1


# 自顶向下
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root, cur):
            nonlocal ans
            if not root:
                ans = max(ans, cur)
                return
            dfs(root.left, cur + 1)
            dfs(root.right, cur + 1)

        dfs(root, 0)
        return ans
