class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        win = (m + n + 1) // 2
        left, right = 0, m
        while left <= right:
            p1 = (left + right) // 2
            p2 = win - p1
            l1 = nums1[p1 - 1] if p1 > 0 else float("-inf")
            r1 = nums1[p1] if p1 < m else float("inf")
            l2 = nums2[p2 - 1] if p2 > 0 else float("-inf")
            r2 = nums2[p2] if p2 < n else float("inf")
            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 1:
                    return float(max(l1, l2))
                else:
                    return float((max(l1, l2) + min(r1, r2)) / 2)
            elif l1 > r2:
                right = p1 - 1
            else:
                left = p1 + 1
