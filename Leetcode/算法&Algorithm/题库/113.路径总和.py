# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def fun(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [[root.val]]
            left = fun(root.left)
            right = fun(root.right)
            return [[root.val] + i for i in left + right]

        res = fun(root)
        ans = []
        for i in res:
            if sum(i) == targetSum:
                ans.append(i)
        return ans
