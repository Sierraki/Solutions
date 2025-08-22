class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        cnt = Counter()
        for c in range(n - 2, 1, -1):
            cnt[nums[c + 1]] += 1
            for a in range(c):
                for b in range(a + 1, c):
                    if (total := nums[a] + nums[b] + nums[c]) in cnt:
                        ans += cnt[total]
        return ans
