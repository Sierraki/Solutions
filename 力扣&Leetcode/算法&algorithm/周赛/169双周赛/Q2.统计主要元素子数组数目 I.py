class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        def fun(res):
            cnt = ans = 0
            for i in range(len(res)):
                if res[i] == target:
                    cnt += 1
                if cnt > (i + 1) / 2:
                    ans += 1
            return ans

        n = len(nums)
        ans = 0
        for i in range(n):
            ans += fun(nums[i:])
        return ans
