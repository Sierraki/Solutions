class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        nums = {idx: i for idx, i in enumerate(gem)}
        for i, j in operations:
            dif = nums[i] // 2
            nums[i] -= dif
            nums[j] += dif
        return max(nums.values()) - min(nums.values())
