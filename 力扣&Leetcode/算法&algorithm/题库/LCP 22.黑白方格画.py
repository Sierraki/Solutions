class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
        if k == 0:
            return 1
        res = []
        for x in range(0, n + 1):
            if n - x > 0:
                y = (k - n * x) // (n - x)
                if n * x + (n - x) * y == k and y >= 0:
                    if y != n:
                        res.append([x, y])
            if n == x:
                if n * x == k:
                    res.append([x, 0])
        ans = 0

        def fun(n, k):
            ans1 = ans2 = ans3 = 1
            tar = max(n, k)
            for i in range(1, tar + 1):
                if i <= n:
                    ans1 *= i
                if i <= k:
                    ans2 *= i
                if i <= n - k:
                    ans3 *= i
            return ans1 // (ans2 * ans3)

        for i, j in res:
            ans += fun(n, i) * fun(n, j)
        return ans
