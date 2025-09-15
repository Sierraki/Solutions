class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        a = b = cnt = 0
        for i in grid:
            a += max(i)
        for i in range(len(grid[0])):
            res = 0
            for j in grid:
                if j[i] != 0:
                    cnt += 1
                res = max(res, j[i])
            b += res
        return a + b + cnt
