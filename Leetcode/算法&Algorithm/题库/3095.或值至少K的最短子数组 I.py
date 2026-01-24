class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def fun(res: list) -> int:
            if len(res) == 1:
                return res[0] | res[0]
            ans = res[0]
            for i in range(1, len(res)):
                ans |= res[i]
            return ans

        ans = -1
        for i in range(len(nums)):
            for j in range(i + 1):
                tar = nums[j : i + 1]
                if fun(tar) >= k:
                    if ans == -1:
                        ans = len(tar)
                    else:
                        ans = min(ans, len(tar))
        return ans
