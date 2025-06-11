class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = 0
        for idx, i in enumerate(str(n)):
            if idx % 2 == 0:
                res += int(i)
            else:
                res -= int(i)
        return res
