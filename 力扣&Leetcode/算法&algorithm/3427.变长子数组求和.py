class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        # right
        right = [i for i in range(len(nums))]
        # left
        left = []
        for idx, i in enumerate(nums):
            ans = max(0, idx - i)
            left.append(ans)
        res = list(zip(left, right))
        s = 0
        res1 = []
        for i in nums:
            s += i
            res1.append(s)
        ans = 0
        for i, j in res:
            if i == j:
                ans += res1[i]
            elif i == 0:
                ans += res1[j]
            else:
                ans += res1[j] - res1[i - 1]
        return ans
