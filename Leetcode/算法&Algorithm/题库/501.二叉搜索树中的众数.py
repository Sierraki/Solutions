# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = deque([root])
        ans = Counter()
        while res:
            cur = res.popleft()
            ans[cur.val] += 1
            if cur.left:
                res.append(cur.left)
            if cur.right:
                res.append(cur.right)
        tar = max(ans.values())
        return [i for i, j in ans.items() if j == tar]
