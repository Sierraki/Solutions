# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def fun(root, cur):
            if not root:
                return
            cur.append(chr(97 + root.val))
            if not root.left and not root.right:
                ans = "".join(cur)[::-1]
                if res:
                    res[-1] = min(res[-1], ans)
                else:
                    res.append(ans)
            else:
                fun(root.left, cur)
                fun(root.right, cur)
            cur.pop()

        res = []
        fun(root, [])
        return res[0]
