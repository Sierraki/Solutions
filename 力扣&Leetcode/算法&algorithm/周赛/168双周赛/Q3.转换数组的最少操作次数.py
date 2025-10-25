class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        # 原数字->目标->终点
        tar = nums2[-1]
        lc = -1

        # 记录最小路径的数字的位置
        def fun(n1=int, tar=int, n2=int) -> int:
            if n1 <= tar <= n2 or n2 <= tar <= n1:
                return 0
            elif n1 <= n2 <= tar or tar <= n2 <= n1:
                return abs(tar - n2)
            elif n2 <= n1 <= tar or tar <= n1 <= n2:
                return abs(tar - n1) * 2

        # 如果直接加答案
        mi = float("inf")
        for i in range(len(nums1)):
            dis = fun(nums1[i], tar, nums2[i])
            if dis < mi:
                mi = dis
        ans1 = 1 + mi
        for i in range(len(nums1)):
            ans1 += abs(nums2[i] - nums1[i])
        # 不换数字直接加
        ans2 = 0
        mi = float("inf")
        for i in nums1:
            mi = min(mi, abs(i - tar))
        for i in range(len(nums1)):
            ans2 += abs(nums1[i] - nums2[i])
        ans2 += mi + 1
        return min(ans1, ans2)