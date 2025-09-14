class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        s = 0
        for idx, i in enumerate(nums):
            if bin(idx).count("1") == k:
                s += i
        return s
