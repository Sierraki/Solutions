class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        for i in range(len(hours)):
            if hours[i] >= 24:
                hours[i] = hours[i] % 24
        cnt = Counter(hours)
        res = 0
        # 0
        if cnt[0] > 1:
            res += cnt[0] * (cnt[0] - 1) // 2
        # 12
        if cnt[12] > 1:
            res += cnt[12] * (cnt[12] - 1) // 2

        nums = [i for i in hours if i != 0 and i != 12]
        c = Counter()
        cc = Counter(nums)
        nums = list(set(nums))
        for i in nums:
            tar = 24 - i
            if i not in c:
                c[tar] = i
            else:
                res += cc[i] * cc[tar]
        return res
