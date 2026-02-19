class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = []
        pin = 0
        cnt = 0
        for i, j in enumerate(s):
            if j != s[pin]:
                res.append(i - pin)
                pin = i
        if pin != len(s):
            res.append(len(s) - pin)
        for i in range(1, len(res)):
            cnt += min((res[i]), (res[i - 1]))
        return cnt
