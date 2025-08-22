class Solution:
    def checkString(self, s: str) -> bool:
        a = 0
        b = float("inf")
        for i in range(len(s)):
            if s[i] == "a":
                a = i
            else:
                b = min(b, i)
        return a < b or a == b == 0
