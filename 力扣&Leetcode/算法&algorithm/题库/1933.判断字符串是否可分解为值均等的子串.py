class Solution:
    def isDecomposable(self, s: str) -> bool:
        l = 0
        res = []
        for i in range(len(s)):
            if s[i] != s[l]:
                res.append(s[l:i])
                l = i
            if i == len(s) - 1:
                res.append(s[l : i + 1])
        cnt1 = 0
        for i in res:
            if len(i) % 3 == 2:
                cnt1 += 1
            elif len(i) % 3 == 1:
                return False
        if cnt1 == 1:
            return True
        return False
