# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res = deque([root])
        ans = []
        while res:
            a = 0
            size = len(res)
            for _ in range(size):
                cur = res.popleft()
                a += cur.val
                if cur.left:
                    res.append(cur.left)
                if cur.right:
                    res.append(cur.right)
            ans.append(a)
        ans.sort(reverse=True)
        if k > len(ans):
            return -1
        return ans[k - 1]
