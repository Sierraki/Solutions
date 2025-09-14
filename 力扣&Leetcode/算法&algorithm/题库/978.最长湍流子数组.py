class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        dp = [0] * len(arr)
        dp[0] = 1
        if arr[0] > arr[1] or arr[0] < arr[1]:
            dp[1] = 2
        for i in range(2, len(dp)):
            if arr[i - 1] < arr[i]:
                if arr[i - 2] > arr[i - 1]:
                    dp[i] = dp[i - 1] + 1
                else:
                    dp[i] = 2
            elif arr[i - 1] > arr[i]:
                if arr[i - 2] < arr[i - 1]:
                    dp[i] = dp[i - 1] + 1
                else:
                    dp[i] = 2
        return max(dp)
