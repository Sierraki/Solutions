class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        l = []
        for i in range(1, n, 2):
            l.append(nums[i])
        return sum(l)
