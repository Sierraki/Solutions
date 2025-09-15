# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = deque([root])
        ans = 0
        while res:
            cur = res.popleft()
            if cur.left:
                res.append(cur.left)
                if not cur.left.left and not cur.left.right:
                    ans += cur.left.val
            if cur.right:
                res.append(cur.right)
        return ans
