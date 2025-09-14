class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        lc1 = nums.index(1)
        cnt = 0
        if lc1 != 0:
            del nums[lc1]
            nums.insert(0, 1)
            cnt += lc1
        lc2 = nums.index(n)
        if lc2 != n - 1:
            cnt += n - (lc2 + 1)
        return cnt
