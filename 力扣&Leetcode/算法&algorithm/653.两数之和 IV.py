# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def fun(root):
            if not root:
                return
            res.append(root.val)
            fun(root.left)
            fun(root.right)

        res = []
        fun(root)
        cnt = Counter()
        for i in res:
            tar = k - i
            if tar not in cnt:
                cnt[i] = tar
            else:
                return True
        return False
