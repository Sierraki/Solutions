# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
