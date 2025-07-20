class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = [int(i) for i in str(s)]

        def fun(s: list) -> list:
            res = []
            for i in range(1, len(s)):
                res.append((s[i] + s[i - 1]) % 10)
            return res

        while len(s) != 2:
            s = fun(s)
        return s[0] == s[1]
