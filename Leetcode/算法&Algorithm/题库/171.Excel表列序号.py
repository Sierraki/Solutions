class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = 0
        s = 0
        num = columnTitle[::-1]
        for i in num:
            ans = (ord(i) - 64) * (26**n)
            n += 1
            s += ans
        return s
