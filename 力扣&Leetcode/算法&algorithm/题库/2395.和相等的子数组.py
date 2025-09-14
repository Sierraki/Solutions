class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        cnt = Counter()
        for i in range(1, len(nums)):
            ans = nums[i] + nums[i - 1]
            if ans not in cnt:
                cnt[ans] = 1
            else:
                return True
        return False
