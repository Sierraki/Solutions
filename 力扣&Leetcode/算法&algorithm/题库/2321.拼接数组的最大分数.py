class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        if n == 1:
            return nums1[0]

        def fun(nums1, nums2):
            res1 = [nums1[i] - nums2[i] for i in range(n)]
            pf = []
            s = 0
            for i in res1:
                s += i
                pf.append(s)
            mi = pf[0]
            ans1 = -float("inf")
            for i in range(1, n):
                mi = min(mi, pf[i - 1])
                ans1 = max(ans1, pf[i], pf[i] - mi)
            return ans1

        return max(sum(nums2) + fun(nums1, nums2), sum(nums1) + fun(nums2, nums1))
