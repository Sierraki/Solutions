class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        mx = 0
        res = []
        for i in nums:
            mx = max(len(bin(i)[2:]), mx)
        for i in nums:
            cur = list(map(int, bin(i)[2:]))
            if len(cur) < mx:
                cur = [0] * (mx - len(cur)) + cur
            res.append(cur)
        ans = []
        for i in range(mx):
            cur = 0
            for j in range(len(res)):
                cur += res[j][i]
            ans.append(cur)
        for i, j in enumerate(ans):
            if j >= k:
                ans[i] = 1
            else:
                ans[i] = 0
        ans1 = int("".join(map(str, ans)), 2)
        return ans1
