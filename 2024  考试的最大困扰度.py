class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        nums = answerKey

        n = len(nums)

        d1 = defaultdict(int)
        wl = 0

        # F --> T
        for i in range(n):
            if d1["F"] < k or (d1["F"] == k and nums[i] == "T"):
                d1[nums[i]] += 1
                wl += 1
            elif d1["F"] > k or (d1["F"] == k and nums[i] == "F"):
                d1[nums[i]] += 1
                d1[nums[i - wl]] -= 1
                if d1[nums[i - wl]] == 0:
                    del d1[nums[i - wl]]

        a = wl

        d2 = defaultdict(int)
        wl = 0

        # F --> T
        for i in range(n):
            if d2["T"] < k or (d2["T"] == k and nums[i] == "F"):
                d2[nums[i]] += 1
                wl += 1
            elif d2["T"] > k or (d2["T"] == k and nums[i] == "T"):
                d2[nums[i]] += 1
                d2[nums[i - wl]] -= 1
                if d2[nums[i - wl]] == 0:
                    del d2[nums[i - wl]]
        b = wl

        return max(a, b)
