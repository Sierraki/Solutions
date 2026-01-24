# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def fun(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [[root.val]]
            left = fun(root.left)
            right = fun(root.right)
            return [[root.val] + i for i in left + right]
        res = fun(root)
        def fun1(nums: list):
            if len(nums) > 1:
                for i in range(len(nums)):
                    if i < len(nums) - 1:
                        nums[i] = str(nums[i]) + "->"
                    else:
                        nums[i] = str(nums[i])
            else:
                return str(nums[0])
            return "".join(nums)


        for i in range(len(res)):
            res[i] = fun1(res[i])
        return res
# 做法2
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root, cur):
            if not root:
                return
            cur.append(root.val)
            if not root.left and not root.right:
                res.append("->".join(map(str, cur)))
            else:
                left = dfs(root.left, cur)
                right = dfs(root.right, cur)
            cur.pop()

        res = []
        dfs(root, [])
        return res
