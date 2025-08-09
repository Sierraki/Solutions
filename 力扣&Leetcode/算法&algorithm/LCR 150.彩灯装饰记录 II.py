# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        res = deque([root])
        while res:
            n = len(res)
            lay = []
            for _ in range(n):
                cur = res.popleft()
                lay.append(cur.val)
                if cur.left:
                    res.append(cur.left)
                if cur.right:
                    res.append(cur.right)
            ans.append(lay)
        return ans
