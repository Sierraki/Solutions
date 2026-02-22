class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        mi = float("inf")
        cnt = 0
        for i in matrix:
            for j in i:
                total += abs(j)
                mi = min(mi, abs(j))
                if j < 0:
                    cnt += 1
        if cnt % 2 == 0:
            return total
        return total - 2 * mi
