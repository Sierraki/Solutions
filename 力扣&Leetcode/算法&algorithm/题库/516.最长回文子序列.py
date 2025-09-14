class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def fun(text1: str, text2: str):
            m = len(text1)
            n = len(text2)
            dp = [[0] * (m + 1) for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if text1[j - 1] == text2[i - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            return dp[-1][-1]

        return fun(s, s[::-1])


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m = len(s)
        dp = [[0] * m for _ in range(m)]
        mx = -float("inf")
        # dp[j][i] i row j Column
        for i in range(m):
            for j in range(i, -1, -1):
                if i == j:
                    dp[j][i] = 1
                else:
                    if s[i] == s[j]:
                        dp[j][i] = dp[j + 1][i - 1] + 2
                    else:
                        dp[j][i] = max(dp[j + 1][i], dp[j][i - 1])
                mx = max(mx, dp[j][i])
        return mx


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m = len(s)
        dp = [[0] * m for _ in range(m)]
        # dp[j][i] i row j Column
        for i in range(m):
            for j in range(i, -1, -1):
                if i == j:
                    dp[j][i] = 1
                else:
                    if s[i] == s[j]:
                        dp[j][i] = dp[j + 1][i - 1] + 2
                    else:
                        dp[j][i] = max(dp[j + 1][i], dp[j][i - 1])
        return dp[0][m - 1]
