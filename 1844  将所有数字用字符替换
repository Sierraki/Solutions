class Solution:
    def replaceDigits(self, s: str) -> str:
        a = []
        for idx, i in enumerate(s):
            if i.isalpha():
                a.append(i)
            else:
                lc = chr(ord(s[idx - 1]) + int(i))
                a.append(lc)
        b = "".join(a)
        return b
