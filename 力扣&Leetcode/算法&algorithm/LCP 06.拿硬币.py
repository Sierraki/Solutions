class Solution:
    def minCount(self, coins: List[int]) -> int:
        res = 0
        for i in coins:
            if i % 2 == 0:
                res += i // 2
            else:
                res += i // 2 + 1
        return res
