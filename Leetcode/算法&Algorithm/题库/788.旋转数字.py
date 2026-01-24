class Solution:
    def rotatedDigits(self, n: int) -> int:
        def fun(x) -> bool:
            x = str(x)
            res = False
            for i in x:
                if i in "347":
                    return False
                if i in "2569":
                    res = True
            return res

        cnt = 0
        for i in range(1, n + 1):
            if fun(i):
                cnt += 1
        return cnt
