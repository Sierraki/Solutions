# 原始做法
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


# 递归做法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res=0
        def dfs(root):
            nonlocal res
            if not root:
                return
            dfs(root.left)
            dfs(root.right)    
            if root.left and not root.left.right and not root.left.left:
                res+=(root.left.val)
                return 
        dfs(root)
        return res
