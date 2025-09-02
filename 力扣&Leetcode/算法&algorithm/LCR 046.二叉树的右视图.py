# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = deque([root])
        ans = []
        while res:
            n = len(res)
            a = []
            for i in range(n):
                cur = res.popleft()
                a.append(cur.val)
                if cur.left:
                    res.append(cur.left)
                if cur.right:
                    res.append(cur.right)
            ans.append(a)
        ans1 = []
        for i in ans:
            ans1.append(i[-1])
        return ans1
