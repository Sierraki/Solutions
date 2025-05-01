class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        k = sum(nums)

        nums += nums
  

        cur = big = sum(nums[:k])

        for i in range(k, n + k):
            cur += nums[i] - nums[i - k]
            big = max(big, cur)
        return(k - big)
