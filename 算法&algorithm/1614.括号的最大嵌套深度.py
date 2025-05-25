class Solution:
    def maxDepth(self, s: str) -> int:
        cur = mx = 0
        for i in s:
            if i == "(":
                cur += 1
            elif i == ")":
                cur -= 1
            mx = max(cur, mx)
        print(mx)
        return mx
