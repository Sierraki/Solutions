class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def check(nums=list) -> bool:
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    return False
            return True

        ans = 0
        while not check(nums):
            lc = 0
            mi = float("inf")
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < mi:
                    mi = nums[i] + nums[i + 1]
                    lc = i
            nums[lc] = mi
            del nums[lc + 1]
            ans += 1
        return ans
