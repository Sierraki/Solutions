class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums1 = sorted(nums)
        cnt = []
        for i in range(len(nums)):
            if nums[i] != nums1[i]:
                cnt.append(i)
        if cnt:
            return cnt[-1] - cnt[0] + 1
        else:
            return 0
