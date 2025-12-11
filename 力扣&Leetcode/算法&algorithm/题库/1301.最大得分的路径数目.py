class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        for i, j in enumerate(board):
            board[i] = [k for k in j]
        board[-1][-1] = "0"
        mod = 10**9 + 7
        n = len(board)
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        for i in range(1, n):
            cur = board[0][i]
            if cur == "X":
                dp[0][i] = [-float("inf"), -float("inf")]
            else:
                dp[0][i][0] = dp[0][i - 1][0] + int(cur)
                if dp[0][i - 1][0] == -float("inf"):
                    dp[0][i][1] = -float("inf")
                else:
                    dp[0][i][1] = 1
        for i in range(1, n):
            cur = board[i][0]
            if cur == "X":
                dp[i][0] = [-float("inf"), -float("inf")]
            else:
                dp[i][0][0] = dp[i - 1][0][0] + int(cur)
                if dp[i - 1][0][0] == -float("inf"):
                    dp[i][0][1] = -float("inf")
                else:
                    dp[i][0][1] = 1
        dp[0][0][1] = 1
        for i in range(1, n):
            for j in range(1, n):
                cur = board[i][j]
                if cur == "X":
                    dp[i][j] = [-float("inf"), -float("inf")]
                else:
                    tar = [dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]]
                    mx = -float("inf")
                    for k in tar:
                        mx = max(mx, k[0])
                    dp[i][j][0] = mx + int(cur)
                    dp[i][j][1] = 0
                    for k1, k2 in tar:
                        if k1 == mx:
                            dp[i][j][1] += k2
        ans = dp[-1][-1]
        if ans[0] == ans[1] == -float("inf"):
            return [0, 0]
        return [ans[0] % mod, ans[1] % mod]
