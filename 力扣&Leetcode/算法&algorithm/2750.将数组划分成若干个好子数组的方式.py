class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        res = []
        for idx, i in enumerate(nums):
            if i == 1:
                res.append(idx)
        if not res:
            return 0
        ans = [1]
        for i in range(1, len(res)):
            ans.append(res[i] - res[i - 1])
        s = 1
        for i in ans:
            s = (s * i) % (10**9 + 7)
        return s
