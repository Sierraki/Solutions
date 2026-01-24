import math


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a = int(math.sqrt(num))
        return a**2 == num
