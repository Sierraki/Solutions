class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumx = sum(nums)
        bu = sum(nums)
        for idx, i in enumerate(nums):
            bu = bu - i
            cur = sumx - bu - i
            if bu == cur:
                return idx
        else:
            return -1
