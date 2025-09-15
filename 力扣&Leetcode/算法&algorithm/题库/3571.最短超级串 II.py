class Solution:
    def shortestSuperstring(self, s1: str, s2: str) -> str:
        if s1 in s2:
            return s2
        if s2 in s1:
            return s1

        def fun(s1: str, s2: str) -> str:
            l, r = len(s1) - 1, 0
            ans = 0
            while l >= 0 and r < len(s2):

                if s1[l:] == s2[: r + 1]:
                    ans = len(s1[l:])
                l -= 1
                r += 1
            return s1 + s2[ans:]

        a = fun(s1, s2)
        b = fun(s2, s1)
        if len(a) <= len(b):
            return a
        return b
