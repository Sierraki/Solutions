class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2:
            return s
        
        ans = s[0]
        m = len(s)
        dp = [[False] * m for _ in range(m)]
        mx = 0

        # 状态转移，先从单列开始从上往下填，再从左到右
        # 先判断左右端点相不相同，然后检查dp[j+1][i-1]是否ture
        # j 为左端点
        # i 为右端点

        for i in range(m):
            for j in range(i + 1):
                # 两端不同
                if s[j] != s[i]:
                    dp[j][i] = False
                # 两端相同
                else:
                    if i - j <= 1:
                        dp[j][i] = True
                    else:
                        # 判定dp[j+1][i-1]
                        dp[j][i] = dp[j + 1][i - 1]
                if dp[j][i] == True and i - j + 1 > mx:
                    mx = i - j + 1
                    ans = s[j : i + 1]
        return ans
