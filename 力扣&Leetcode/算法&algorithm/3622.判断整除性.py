class Solution:
    def checkDivisibility(self, n: int) -> bool:
        res = [int(i) for i in str(n)]
        s = 1
        for i in res:
            s *= i
        return n % (s + sum(res)) == 0
