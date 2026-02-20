from bisect import bisect, bisect_left


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                a, b, c = nums[i], nums[j], nums[j + 1]
                if a + b > c:
                    left, right = j + 1, bisect_left(nums, a + b)
                    ans += right - left
        return ans
