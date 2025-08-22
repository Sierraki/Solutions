# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def fun(root: TreeNode) -> list[int]:
            if not root:
                return
            fun(root.left)
            res.append(root.val)
            fun(root.right)

        res = []
        fun(root)
        return res


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            return (
                self.inorderTraversal(root.left)
                + [root.val]
                + self.inorderTraversal(root.right)
            )
