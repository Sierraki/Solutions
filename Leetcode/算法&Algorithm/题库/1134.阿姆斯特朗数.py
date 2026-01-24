class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = len(str(n))
        s = 0
        for i in str(n):
            s += int(i) ** k
        return s == n
