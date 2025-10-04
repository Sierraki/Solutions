class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def fun(res=list) -> int:
            cnt = 0
            if "R" in res:
                lc = lc1 = res.index("R")
            else:
                return 0
            # <--
            while 0 <= lc < 8:
                if lc >= 0 and res[lc] == "B":
                    break
                elif lc >= 0 and res[lc] == "p":
                    cnt += 1
                    break
                lc -= 1
            # -->
            while 0 <= lc1 < 8:
                if lc1 < 8 and res[lc1] == "B":
                    return cnt
                elif lc1 < 8 and res[lc1] == "p":
                    cnt += 1
                    break
                lc1 += 1
            return cnt

        ans = 0
        for i in board:
            ans += fun(i)
        grid = board.copy()
        for i in range(8):
            for j in range(i, 8):
                grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
        for i in board:
            ans += fun(i)
        return ans
