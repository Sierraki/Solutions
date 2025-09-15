class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        ans = -1
        for idx, i in enumerate(nums):
            if idx % 10 == i:
                ans = idx
                return ans
        return ans
