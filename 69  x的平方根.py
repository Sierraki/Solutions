class Solution:
    def mySqrt(self, x: int) -> int:

        i = 0

        while i**2 < x and i < x:

            if i**2 < x and (i + 1) ** 2 < x:
                i += 1

            if i**2 < x and (i + 1) ** 2 == x:
                i += 1

            if i**2 < x and (i + 1) ** 2 > x:
                break

        return i
