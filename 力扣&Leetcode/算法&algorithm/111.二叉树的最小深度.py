# 深度优先 DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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


# 广度优先 BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
