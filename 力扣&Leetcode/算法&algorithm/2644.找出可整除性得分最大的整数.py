class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ans = []
        for i in divisors:
            res = 0
            for j in nums:
                if j % i == 0:
                    res += 1
            ans.append([i, res])
        ans.sort(key=lambda x: (-x[1], x[0]))
        return ans[0][0]
