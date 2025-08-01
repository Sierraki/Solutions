class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        cnt = Counter()
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            ans = (nums[l] + nums[r]) / 2
            cnt[ans] += 1
            l += 1
            r -= 1
        return len(cnt)
