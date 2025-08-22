class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for i in range(0, len(nums), 3):
            if max(cnt.values()) == 1:
                return ans
            a = nums[i : i + 3]
            for j in a:
                cnt[j] -= 1
            ans += 1
        return ans
