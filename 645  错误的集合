class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        b = [i for i in range(1, len(nums) + 1)]
        aa = sum(b) - sum(set(nums))  # 缺失值
        h = sum(nums) - sum(set(nums))
        return [h, aa]
