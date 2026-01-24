class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def fun(matrix):
            res = [[0] * n for _ in range(n)]
            for i in range(n):
                tar = max(matrix[i])
                for j in range(n):
                    if tar - matrix[i][j] < 0:
                        res[i][j] = 0
                    else:
                        res[i][j] = tar - matrix[i][j]
            return res

        def re(matrix):
            re_grid = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    re_grid[j][i] = matrix[i][j]
            return re_grid

        res1 = fun(grid)
        res2 = re(fun(re(grid)))
        ans = 0
        for i in range(n):
            for j in range(n):
                ans += min(res1[i][j], res2[i][j])
        return ans
