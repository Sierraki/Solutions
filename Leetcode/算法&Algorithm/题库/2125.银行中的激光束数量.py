class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        nums = [i.count("1") for i in bank if i.count("1") != 0]
        ans = 0
        for i in range(1, len(nums)):
            ans += nums[i - 1] * nums[i]
        return ans
