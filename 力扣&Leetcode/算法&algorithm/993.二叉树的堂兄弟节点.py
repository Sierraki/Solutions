# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        res = deque([root])
        ans = []
        while res:
            n = len(res)
            a = []
            for _ in range(n):
                cur = res.popleft()
                if cur:
                    res.append(cur.left)
                    res.append(cur.right)
                    a.append(cur.val)
                else:
                    a.append(None)
            ans.append(a)
        for idx, i in enumerate(ans):
            if x in i and y in i and idx > 1:
                for j in range(1, len(i), 2):
                    if (i[j] == x and i[j - 1] == y) or (i[j] == y and i[j - 1] == x):
                        return False
                else:
                    return True
        return False
