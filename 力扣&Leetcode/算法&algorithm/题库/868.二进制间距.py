class Solution:
    def binaryGap(self, n: int) -> int:
        cnt = defaultdict(list)
        for idx, i in enumerate(bin(n)[2:]):
            if i == "1":
                cnt[i].append(idx)
        res = cnt["1"]
        if len(res) <= 1:
            return 0
        mx = 0
        for i in range(1, len(res)):
            mx = max(mx, res[i] - res[i - 1])
        return mx
