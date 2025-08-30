class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(i + 1):
                if s[j : i + 1] == s[j : i + 1][::-1]:
                    ans += 1
        return ans
