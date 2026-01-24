class Solution:
    def sumOfMultiples(self, n: int) -> int:
        res = 0
        for i in range(1, n + 1):
            if i % 3 == 0:
                res += i
            elif i % 5 == 0:
                res += i
            elif i % 7 == 0:
                res += i
        return res
