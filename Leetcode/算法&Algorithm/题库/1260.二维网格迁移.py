class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # 逆时针90
        m = len(grid)
        n = len(grid[0])
        res = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                res[i][j] = grid[j][i]

        def fun(res=list) -> list:
            cur = res[-1]
            cur.insert(0, cur[-1])
            del cur[-1]
            res.insert(0, cur)
            del res[-1]
            return res

        for _ in range(k):
            res = fun(res)
        ans = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                ans[j][i] = res[i][j]
        return ans
