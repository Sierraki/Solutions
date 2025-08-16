class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n - 2) * (n - 1) * n / 6
        cnt = Counter(nums)
        res1 = {i: j for i, j in cnt.items() if j > 1}
        res2 = [i for i in nums if i not in res1]
        # 2
        ans1 = ans2 = 0
        for i, j in res1.items():
            p1 = [jj for ii, jj in res1.items() if ii != i]
            print(p1)
            if j >= 2:
                # 2
                ans1 += (j * (j - 1) / 2) * (sum(p1) + len(res2))
            if j >= 3:
                ans2 += j * (j - 1) * (j - 2) / 6
        return int(total - ans1 - ans2)
