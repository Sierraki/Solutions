# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = deque([root])
        ans = []
        while res:
            cur = res.popleft()
            ans.append(cur.val)
            if cur.left:
                res.append(cur.left)
            if cur.right:
                res.append(cur.right)
        ans.sort()
        mi = float("inf")
        for i in range(1, len(ans)):
            mi = min(mi, abs(ans[i] - ans[i - 1]))
        return mi
