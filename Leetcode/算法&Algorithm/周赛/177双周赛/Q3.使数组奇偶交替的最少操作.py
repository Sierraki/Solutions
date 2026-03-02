class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return [0, 0]
        # oeoe
        ans1 = []
        res1 = []
        for i, j in enumerate(nums, 1):
            if j % 2 == i % 2:
                res1.append(j)
            else:
                ans1.append(j)
        # eoeo
        ans2 = []
        res2 = []
        for i, j in enumerate(nums):
            if j % 2 == i % 2:
                res2.append(j)
            else:
                ans2.append(j)
        # ans为变，res为不变
        print(ans1, res1)
        # print(ans2, res2)

        def fun(ans, res):
            if not ans:
                return max(res) - min(res)
            ans.sort()
            mx = max(res) if res else -float("inf")
            mi = min(res) if res else float("inf")
            mi_diff = float("inf")
            for i in range(len(ans) + 1):

                mx_left = ans[i - 1] + 1 if i > 0 else -float("inf")
                mi_left = ans[0] + 1 if i > 0 else float("inf")

                mx_right = ans[-1] - 1 if i < len(ans) else -float("inf")
                mi_right = ans[i] - 1 if i < len(ans) else float("inf")

                cur_mx = max(mx, mx_left, mx_right)
                cur_mi = min(mi, mi_left, mi_right)
                mi_diff = min(mi_diff, cur_mx - cur_mi)
            print(mx_left, mi_left, mx_right, mi_right, cur_mx, cur_mi, mi_diff)

            return mi_diff

        a, b = fun(ans1, res1), fun(ans2, res2)

        if len(ans1) < len(ans2):
            return [len(ans1), a]
        elif len(ans1) > len(ans2):
            return [len(ans2), b]
        else:
            return [len(ans2), min(a, b)]
