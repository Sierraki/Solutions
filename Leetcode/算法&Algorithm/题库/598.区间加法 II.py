class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if ops == []:
            return m * n
        res1 = [i for i, j in ops]
        res2 = [j for i, j in ops]
        return min(res1) * min(res2)
