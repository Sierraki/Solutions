class Solution:

    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        if n == 1:
            for i in range(1, m):
                if grid[i - 1] != grid[i]:
                    return False
            return True
        else:
            # down
            for i in range(1, m):
                for j in range(n):
                    if grid[i][j] != grid[i - 1][j]:
                        return False
            for i in range(m):
                for j in range(1, n):
                    if grid[i][j] == grid[i][j - 1]:
                        return False
            return True
