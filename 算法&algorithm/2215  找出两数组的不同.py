class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a = []
        b = []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        for i in nums1:
            if i not in nums2:
                a.append(i)
        for i in nums2:
            if i not in nums1:
                b.append(i)
        return [a, b]
