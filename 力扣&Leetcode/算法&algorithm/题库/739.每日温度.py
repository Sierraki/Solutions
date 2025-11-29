class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nums = [[i, j] for i, j in enumerate(temperatures)]
        ans = [0] * len(temperatures)
        res = []
        while nums:
            cur = nums[0]
            if not res:
                res.append(cur)
            else:
                while res and cur[1] > res[-1][1]:
                    ans[res[-1][0]] = cur[0] - res[-1][0]
                    res.pop()
                res.append(cur)
            del nums[0]
        for i, j in res:
            ans[i] = 0
        return ans
