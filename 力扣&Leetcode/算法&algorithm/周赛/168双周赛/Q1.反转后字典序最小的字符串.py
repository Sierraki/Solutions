class Solution:
    def lexSmallest(self, s: str) -> str:
        ans = s
        for i in range(len(s)):
            p1 = s[: i + 1]
            p2 = s[i + 1 :]
            res1 = p1[::-1] + p2
            res2 = p1 + p2[::-1]
            ans = min(ans, res1, res2)
        return ans