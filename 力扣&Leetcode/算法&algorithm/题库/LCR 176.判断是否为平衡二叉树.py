# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def height(root=TreeNode):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            return 1 + max(left, right)

        res = deque([root])
        while res:
            n = len(res)
            for i in range(n):
                cur = res.popleft()
                left = height(cur.left)
                right = height(cur.right)
                if cur.left:
                    res.append(cur.left)
                if cur.right:
                    res.append(cur.right)
                if abs(left - right) > 1:
                    return False
        return True
