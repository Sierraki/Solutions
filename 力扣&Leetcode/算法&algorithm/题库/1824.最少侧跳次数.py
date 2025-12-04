class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [[0] + [float("inf")] * (n - 1) for _ in range(4)]
        dp[1][1] = 1
        dp[2][1] = 0
        dp[3][1] = 1
        for i in range(1, n):
            cur = obstacles[i]
            if i == 1:
                dp[cur][1] = float("inf")
            else:
                tar = [dp[j][i - 1] for j in [1, 2, 3]]
                for row1 in [1, 2, 3]:
                    if row1 != cur:
                        for idx, row2 in enumerate(tar, start=1):
                            if row2 == float("inf"):
                                dp[row1][i] = min(dp[row1][i], min(tar) + 2)
                                continue
                            else:
                                # 同行
                                if idx == row1:
                                    dp[row1][i] = min(dp[row1][i], dp[row1][i - 1])
                                # 不同行
                                else:
                                    if cur == idx:
                                        continue
                                    else:
                                        dp[row1][i] = min(dp[row1][i], row2 + 1)
        ans = float("inf")
        for i in [1, 2, 3]:
            ans = min(ans, dp[i][-1])
        return ans
