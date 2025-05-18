class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            while n > 0:
                if n % 3 == 0:
                    n = n / 3
                elif n % 5 == 0:
                    n = n / 5
                elif n % 2 == 0:
                    n = n / 2
                else:
                    break
            if n == 1:
                return True
            else:
                return False