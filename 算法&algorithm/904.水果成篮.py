class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        nums = fruits

        cnt = defaultdict(int)

        cur = 0

        n = len(nums)

        for i in range(n):
            if not cnt or (len(cnt) < 2) or (len(cnt) == 2 and cnt[nums[i]] != 0):
                cnt[nums[i]] += 1
                cur += 1
            else:
                cnt[nums[i]] += 1
                cnt[nums[i - cur]] -= 1
                if cnt[nums[i - cur]] == 0:
                    del cnt[nums[i - cur]]

            # print(dict(cnt), nums[i - cur + 1 : i + 1], cur)
        return cur
