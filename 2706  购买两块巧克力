class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        target = sum(prices[:2])
        if target <= money:
            return money - target
        else:
            return money
