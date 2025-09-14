# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res = deque([root])
        ans = []
        while res:
            a = []
            size = len(res)
            for _ in range(size):
                cur = res.popleft()
                a.append(cur.val)
                if cur.left:
                    res.append(cur.left)
                if cur.right:
                    res.append(cur.right)
            ans.append(a)
        for i in range(len(ans)):
            ans[i] = sum(ans[i]) / len(ans[i])
        return ans
