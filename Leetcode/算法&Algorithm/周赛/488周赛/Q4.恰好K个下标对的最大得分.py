class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        m = len(nums2)
        tmp = [[-float("inf")] * m for _ in range(n)]
        dp = [[[-float("inf")] * m for _ in range(n)] for _ in range(k + 1)]
        for i in range(n):
            for j in range(m):
                if i == j == 0:
                    tmp[i][j] = nums1[i] * nums2[j]
                elif i == 0:
                    tmp[i][j] = max(nums1[i] * nums2[j], tmp[i][j - 1])
                elif j == 0:
                    tmp[i][j] = max(nums1[i] * nums2[j], tmp[i - 1][j])

                if i > 0 and j > 0:
                    tmp[i][j] = max(
                        nums1[i] * nums2[j],
                        tmp[i - 1][j - 1],
                        tmp[i - 1][j],
                        tmp[i][j - 1],
                    )
        dp[1] = tmp
        for i in range(2, len(dp)):
            pre = dp[i - 1]
            for ii in range(i - 1, n):
                for jj in range(i - 1, m):
                    cur_val = nums1[ii] * nums2[jj]
                    res1 = cur_val + pre[ii - 1][jj - 1]
                    row = dp[i][ii - 1][jj] if ii > 0 else -float("inf")
                    col = dp[i][ii][jj - 1] if jj > 0 else -float("inf")
                    dp[i][ii][jj] = max(res1, row, col, dp[i][ii][jj])
        return dp[-1][-1][-1]
