class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = Counter()
        ans = 0
        for i in nums:
            tar = i - k
            if tar in cnt:
                ans += cnt[tar]
            cnt[i] += 1
        return ans
