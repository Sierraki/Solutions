class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        lc1 = lc2 = float("inf")
        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                lc1 = i - 1
                break
        else:
            lc1 = 0
        for i in range(n - 1, lc1 - 1, -1):
            if nums[i] > nums[lc1]:
                lc2 = i
                break
        else:
            lc2 = 0
        if lc1 != float("inf") and lc2 != float("inf"):
            nums[lc1], nums[lc2] = nums[lc2], nums[lc1]
        if not (lc1 == lc2 == 0):
            l, r = lc1 + 1, n - 1
        else:
            l, r = 0, n - 1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
