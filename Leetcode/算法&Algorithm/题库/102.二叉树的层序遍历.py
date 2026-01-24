# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        return ans


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[Optional[int]]]:
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
                    res.append(cur.left)
                    res.append(cur.right)
                else:
                    a.append(None)
            if any(item is not None for item in a):
                ans.append(a)
        return ans
