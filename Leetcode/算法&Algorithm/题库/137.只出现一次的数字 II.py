class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for i, j in cnt.items():
            if j == 1:
                return i
