class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = max(nums)
        b = min(nums)
        for i in range(1, b + 1):
            if a % i == 0 and b % i == 0:
                ans = i
        return ans
