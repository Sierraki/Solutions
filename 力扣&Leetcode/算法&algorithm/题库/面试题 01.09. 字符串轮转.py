class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        s1 += s1
        return s2 in s1
