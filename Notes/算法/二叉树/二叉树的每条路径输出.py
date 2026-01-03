def fun(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [[root.val]]
    left=fun(root.left)
    right=fun(root.right)
    return [[root.val]+i for i in left+right]


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root, cur):
            if not root:
                return
            cur.append(root.val)
            if not root.left and not root.right:
                res.append("->".join(map(str, cur)))
            else:
                dfs(root.left, cur)
                dfs(root.right, cur)
            cur.pop()

        res = []
        dfs(root, [])
        return res
