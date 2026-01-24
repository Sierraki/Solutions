class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res0 = []
        res1 = []
        res2 = []
        for i in nums:
            if i % 3 == 0:
                res0.append(i)
            elif i % 3 == 1:
                res1.append(i)
            else:
                res2.append(i)
        res0.sort(reverse=True)
        res1.sort(reverse=True)
        res2.sort(reverse=True)
        ans1 = ans2 = ans3 = ans4 = 0
        if len(res0) >= 3:
            ans1 = sum(res0[:3])
        if len(res0) >= 1 and len(res1) >= 1 and len(res2) >= 1:
            ans2 = res0[0] + res1[0] + res2[0]
        if len(res1) >= 3:
            ans3 = sum(res1[:3])
        if len(res2) >= 3:
            ans4 = sum(res2[:3])
        return max(ans1, ans2, ans3, ans4)
