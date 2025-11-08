class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        left = [1] * n
        for i in range(1, n):
            if nums[i] >= nums[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
        right = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                right[i] = right[i + 1] + 1
            else:
                right[i] = 1
        mx = max(left) if left else 0
        for i in range(n):
            if i > 0:
                left1 = left[i - 1]
            else:
                left1 = 0
            if i < n - 1:
                right1 = right[i + 1]
            else:
                right1 = 0
            if i == 0:
                mx = max(mx, 1 + right1)
            elif i == n - 1:
                mx = max(mx, left1 + 1)
            else:
                if nums[i - 1] <= nums[i + 1]:
                    cur = left1 + 1 + right1
                    mx = max(mx, cur)
                else:
                    res1 = left1 + 1
                    res2 = 1 + right1
                    mx = max(mx, res1, res2)
        return mx
