class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10**9 + 7
        # prefix
        s = 0
        res = []
        for i in arr:
            s += i
            res.append(s)
        ans1 = max(0, res[0])
        mi = float("inf")
        for i in range(1, len(res)):
            mi = min(res[i - 1], mi)
            ans1 = max(ans1, res[i] - mi, res[i])
        ans3 = max(max(res), 0)
        # suffix
        s = 0
        res = []
        for i in range(len(arr) - 1, -1, -1):
            s += arr[i]
            res.insert(0, s)
        ans2 = max(max(res), 0)
        if k == 1:
            return ans1 % mod
        elif k == 2:
            return (max(ans1, ans3 + ans2)) % mod
        else:
            if sum(arr) > 0:
                return (ans3 + ans2 + (k - 2) * sum(arr)) % mod
            else:
                return max(ans1, ans3 + ans2) % mod
