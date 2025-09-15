# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        ans = []
        res = deque([root])
        while res:
            cur = res.popleft()
            ans.append(cur.val)
            if cur.left:
                res.append(cur.left)
            if cur.right:
                res.append(cur.right)
        cnt = Counter()
        for i in ans:
            tar = k - i
            if tar not in cnt:
                cnt[i] = tar
            else:
                return True
        return False
