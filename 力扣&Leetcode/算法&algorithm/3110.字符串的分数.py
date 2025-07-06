class Solution:
    def scoreOfString(self, s: str) -> int:
        c = 0
        for i in range(len(s) - 1):
            c += abs(ord(s[i]) - ord(s[i + 1]))
        return c
