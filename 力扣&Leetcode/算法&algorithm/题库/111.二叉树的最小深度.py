class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        mi = float("inf")
        if root.left:
            mi = min(self.minDepth(root.left), mi)
        if root.right:
            mi = min(self.minDepth(root.right), mi)
        return mi + 1


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = deque([root])
        ans = []
        while res:
            n = len(res)
            a = []
            for _ in range(n):
                cur = res.popleft()
                if not cur.left and not cur.right:
                    return len(ans) + 1
                if cur.left:
                    res.append(cur.left)
                    a.append(cur.left.val)
                if cur.right:
                    res.append(cur.right)
                    a.append(cur.right.val)
            ans.append(a)


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.right:
            return 1 + self.minDepth(root.left)
        if not root.left:
            return 1 + self.minDepth(root.right)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
