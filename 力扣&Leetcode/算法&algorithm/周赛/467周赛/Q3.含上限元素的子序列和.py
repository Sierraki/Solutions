class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n = len(nums)
        answer = [False] * n
        nums.sort()
        dp = [False] * (k + 1)
        dp[0] = True
        i = 0
        for x in range(1, n + 1):
            while i < n and nums[i] <= x:
                num = nums[i]
                for j in range(k, num - 1, -1):
                    if dp[j - num]:
                        dp[j] = True
                i += 1
            cnt = n - i
            for j in range(k + 1):
                if dp[j]:
                    left = k - j
                    if left >= 0 and left % x == 0:
                        tar = left // x
                        if tar <= cnt:
                            answer[x - 1] = True
                            break
        return answer