class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        tar = s[::-1]
        for i in range(1, len(s)):
            if s[i - 1 : i + 1] in tar:
                return True
        return False
