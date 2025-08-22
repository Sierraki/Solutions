class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n
        for i in range(n):
            for j in wordDict:
                if i + 1 >= len(j):
                    if s[i - len(j) + 1 : i + 1] == j:
                        if s[: i - len(j) + 1] == "" or dp[i - len(j)] == True:
                            dp[i] = True
        return dp[-1]
