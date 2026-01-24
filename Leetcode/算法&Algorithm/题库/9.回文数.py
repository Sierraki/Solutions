class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = str(s)
        a = []
        b = []
        lens = len(s)
        for i in range(lens):
            a.append(s[i])
            b.append(s[lens - 1 - i])
        return a == b
