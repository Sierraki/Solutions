# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return []
        res = deque([root])
        ans = []
        while res:
            a = []
            size = len(res)
            for _ in range(size):
                cur = res.popleft()
                if cur:
                    a.append(cur.val)
                    # 将子节点加入队列
                    res.append(cur.left)
                    res.append(cur.right)
                else:
                    a.append(None)
            ans.append(a)
        for i in ans:
            if not (i == i[::-1]):
                return False
        return True
