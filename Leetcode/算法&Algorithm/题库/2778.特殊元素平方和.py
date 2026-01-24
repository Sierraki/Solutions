class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for idx, i in enumerate(nums, start=1):
            if n % idx == 0:
                ans += i**2
        return ans
