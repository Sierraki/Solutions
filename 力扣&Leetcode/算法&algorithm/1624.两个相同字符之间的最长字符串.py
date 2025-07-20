class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        cnt = defaultdict(list)
        for idx, i in enumerate(s):
            cnt[i].append(idx)

        def fun(nums: list) -> int:
            mx = nums[-1] - nums[0] - 1 - Counter(nums[min(nums) : max(nums) + 1])[i]
            return mx

        mx = -float("inf")
        for i, j in cnt.items():
            mx = max(mx, fun(j))
        if mx == -float("inf"):
            return -1
        return mx
