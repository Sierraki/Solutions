class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        nz_cnt = z_cnt = 0
        n = len(grid)
        for i in range(n):
            if grid[i][i] != 0:
                nz_cnt += 1
        for i in range(n - 1, -1, -1):
            if grid[i][i] != 0:
                nz_cnt += 1
        for i in grid:
            for j in i:
                if j != 0:
                    z_cnt += 1
        if n % 2 == 0:
            return z_cnt == nz_cnt
        else:
            return z_cnt == nz_cnt - 1
