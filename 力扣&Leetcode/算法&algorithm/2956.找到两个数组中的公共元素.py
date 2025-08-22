class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        a1 = a2 = 0
        for i in cnt1.keys():
            if i in cnt2:
                a1 += cnt2[i]
        for i in cnt2.keys():
            if i in cnt1:
                a2 += cnt1[i]
        return [a2, a1]
