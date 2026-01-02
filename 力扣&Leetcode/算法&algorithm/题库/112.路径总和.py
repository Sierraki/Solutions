# 迭代做法
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # 节点
        node = deque([root])
        # 路径和
        res = deque([root.val])
        while node:
            cur = node.popleft()
            curres = res.popleft()
            if cur.left:
                node.append(cur.left)
                res.append(curres + cur.left.val)
            if cur.right:
                node.append(cur.right)
                res.append(curres + cur.right.val)
            if not cur.left and not cur.right:
                if targetSum == curres:
                    return True
        return False
# 递归做法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, cur):
            if not root:
                return
            cur += root.val
            dfs(root.left, cur)
            if not root.left and not root.right:
                res.append(cur)
                return
            dfs(root.right, cur)
            cur -= root.val

        res = []
        dfs(root, 0)
        return targetSum in res
