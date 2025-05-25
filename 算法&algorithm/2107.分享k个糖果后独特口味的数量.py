class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        nums = candies
        n = len(nums)
        j = n - k
        cnt = defaultdict(int)
        nums += nums
        for i in range(n - j, n):
            cnt[nums[i]] += 1
        big = cur = len(cnt)
        for i in range(n, n + j):
            # print(nums[i - j + 1], nums[i])
            cnt[nums[i]] += 1
            cnt[nums[i - j]] -= 1
            if cnt[nums[i - j]] == 0:
                del cnt[nums[i - j]]
            cur = len(cnt)
            big = max(cur, big)

        return big
