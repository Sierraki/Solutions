class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(nums1)
        for idx, i in enumerate(nums1):
            lc = nums2.index(i)
            for j in range(lc, len(nums2)):
                if nums2[j] > i:
                    res[idx] = nums2[j]
                    break
        return res
