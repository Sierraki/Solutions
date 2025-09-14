class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 2
        mul = 1
        left = 0
        for right, x in enumerate(nums):
            while gcd(mul, x) > 1:
                mul //= nums[left]
                left += 1
            mul *= x
            ans = max(ans, right - left + 1)
        return ans
