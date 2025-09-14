class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        a = nums.copy()
        nums.sort(reverse=True)
        n = len(nums)
        # nums[0]为最大值
        stat = True
        for i in range(1, n):
            if nums[0] < 2 * nums[i]:
                stat = False
                break
        if stat == False:
            return -1
        else:
            return a.index(nums[0])
