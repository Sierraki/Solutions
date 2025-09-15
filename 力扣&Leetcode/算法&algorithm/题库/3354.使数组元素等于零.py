class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            if nums[i] == 0:
                res.append(i)
        ans = []
        s = 0
        for i in nums:
            s += i
            ans.append(s)
        cnt = 0
        for i in res:
            if ans[i] - nums[i] == ans[-1] - ans[i]:
                cnt += 2
            elif abs(ans[i] - nums[i] - ans[-1] + ans[i]) == 1:
                cnt += 1
        return cnt
