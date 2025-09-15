class Solution:
    def isThree(self, n: int) -> bool:
        res = set()
        for i in range(1, floor(sqrt(n)) + 1):
            if n % i == 0:
                res.add(i)
                res.add(n // i)
        return len(res) == 3
