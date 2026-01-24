class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        def fun(x: int):
            res1 = x % 10
            res2 = x // 10
            if res1 < 5:
                return res2
            else:
                return res2 + 1

        return 100 - fun(purchaseAmount) * 10
