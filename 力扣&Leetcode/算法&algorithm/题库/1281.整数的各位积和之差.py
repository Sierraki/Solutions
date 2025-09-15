class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        m = 1
        j = 0
        for i in str(n):
            m = int(m) * int(i)
        for i in str(n):
            j = int(j) + int(i)
        return m - j
