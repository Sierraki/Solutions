class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = grid[j][i]
        ans = 0
        for i in res:
            for j in range(1, n):
                if i[j] <= i[j - 1]:
                    ans += i[j - 1] - i[j] + 1
                    i[j] = i[j - 1] + 1
        return ans
