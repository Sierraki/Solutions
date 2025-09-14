class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        def fun(nums: list) -> list:
            res = []
            for i in range(0, len(nums), 2):
                if i % 4 == 0:
                    ans = min(nums[i], nums[i + 1])
                else:
                    ans = max(nums[i], nums[i + 1])
                res.append(ans)
            return res

        while len(nums) >= 2:
            nums = fun(nums)
        return nums[0]
