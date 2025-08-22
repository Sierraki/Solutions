class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        if len(nums) == 1:
            return nums[0] + 1
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 != nums[i]:
                ans = i - 1
                break
        else:
            ans = i
        res = sum(nums[: ans + 1])
        while res in cnt:
            res += 1
        return res
