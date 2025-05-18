class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = []
        nums1 = nums[:n]
        nums2 = nums[n:]
        left = 0
        for i in nums2:
            l.append(nums1[left])
            left += 1
            l.append(i)
        return l
