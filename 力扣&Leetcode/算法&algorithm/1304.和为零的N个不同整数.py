class Solution:
    def sumZero(self, n: int) -> List[int]:
        res1 = [i for i in range(1, n // 2 + 1)]
        res2 = [-i for i in range(1, n // 2 + 1)]
        if n % 2 == 1:
            return res1 + res2 + [0]
        return res1 + res2
