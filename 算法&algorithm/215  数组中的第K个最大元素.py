import bisect
class Solution:
    def findKthLargest(self, nums, k) -> int:
        a = sorted(nums[:k])
        for i in range(k, len(nums)):
            if nums[i] > a[0]:
                bisect.insort(a, nums[i])
                del a[0]
        return a[0]
