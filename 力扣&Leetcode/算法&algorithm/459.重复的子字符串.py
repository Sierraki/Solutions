class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        a = s + s
        lc = a.find(s, 1)
        return lc != n
