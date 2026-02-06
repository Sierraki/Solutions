class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = [-1]
        ans = 0
        for i, j in enumerate(s):
            if j == "(":
                res.append(i)
            else:
                res.pop()
                if not res:
                    res.append(i)
                else:
                    ans = max(ans, i - res[-1])
        return ans
