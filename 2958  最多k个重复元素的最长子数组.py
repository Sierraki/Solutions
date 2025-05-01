class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = defaultdict(int)

        left = cur = big = 0

        for i in range(n):
            cnt[nums[i]] += 1
            if cnt[nums[i]] > k:
                while cnt[nums[i]] > k:
                    cnt[nums[left]] -= 1
                    if cnt[nums[left]] == 0:
                        del cnt[nums[left]]
                    left += 1

            cur = i - left + 1
            big = max(cur, big)

        return big
