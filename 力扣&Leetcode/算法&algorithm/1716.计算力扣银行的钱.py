class Solution:
    def totalMoney(self, n: int) -> int:
        ans1 = n // 7
        ans2 = n % 7
        res = ans1 * 28 + (ans1) * (ans1 - 1) // 2 * 7
        if ans2 > 0:
            for i in range(1, ans2 + 1):
                res += i + ans1
        return res
