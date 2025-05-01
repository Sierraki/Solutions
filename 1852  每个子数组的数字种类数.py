class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        wl = 0
        cnt = defaultdict(int)
        a = []

        for i in range(k):
            cnt[nums[i]] += 1
        a.append(len(cnt))

        for i in range(k, n):

            cnt[nums[i]] += 1
            cnt[nums[i - k]] -= 1
            if cnt[nums[i - k]] == 0:
                del cnt[nums[i - k]]
            a.append(len(cnt))

        return a
