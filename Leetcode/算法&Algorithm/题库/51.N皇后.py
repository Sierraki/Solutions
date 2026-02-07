class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        nums = [["."] * n for _ in range(n)]
        dig45 = [True] * (2 * n - 1)
        dig135 = [True] * (2 * n - 1)
        col = [True] * n
        res = []

        #  当前行
        def dfs(cur):
            if cur == n:
                tmp = ["".join(row) for row in nums]
                res.append(tmp)
                return
            for i in range(n):
                if col[i] and dig45[cur + i] and dig135[cur - i + n - 1]:
                    nums[cur][i] = "Q"
                    col[i] = dig45[cur + i] = dig135[cur - i + n - 1] = False
                    dfs(cur + 1)
                    nums[cur][i] = "."
                    col[i] = dig45[cur + i] = dig135[cur - i + n - 1] = True

        dfs(0)
        return res
