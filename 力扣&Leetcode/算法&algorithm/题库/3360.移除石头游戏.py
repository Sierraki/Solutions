class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False
        a = (-21 + sqrt(21**2 - 8 * n)) // (-2)
        if (11 - a) * a <= n:
            a += 1
        if a % 2 == 1:
            return False
        return True
