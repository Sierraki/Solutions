class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        n = len(nums)
        wl = 1
        o = 0
        z = 0
        cnt[nums[0]] += 1
        for i in range(1, n):
            if (cnt[0] == 1 and nums[i] == 1) or cnt[0] == 0:
                cnt[nums[i]] += 1
                o = cnt[1]
                wl += 1
                z = cnt[0]
            else:
                cnt[nums[i]] += 1
                cnt[nums[i - wl]] -= 1
                if cnt[nums[i - wl]] == 0:
                    del cnt[nums[i - wl]]
        if z != 0:
            return o
        else:
            return wl - 1
