# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def fun(root: TreeNode) -> list:
            if not root:
                return
            res.append(root.val)
            fun(root.left)
            fun(root.right)

        res = []
        fun(root)
        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = deque([root])
        res = []
        while stack:
            if not root:
                return []
            else:
                ans = stack.pop()
                res.append(ans.val)
                if ans.right:
                    stack.append(ans.right)
                if ans.left:
                    stack.append(ans.left)
        return res
