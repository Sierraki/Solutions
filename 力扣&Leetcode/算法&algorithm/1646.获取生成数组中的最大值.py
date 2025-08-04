class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
        nums = [0] * (n + 1)
        nums[0] = 0
        nums[1] = 1
        for i in range(n + 1):
            if i > 1:
                if i % 2 == 1:
                    nums[i] = nums[i // 2] + nums[i // 2 + 1]
                else:
                    nums[i] = nums[i // 2]
        return max(nums)
