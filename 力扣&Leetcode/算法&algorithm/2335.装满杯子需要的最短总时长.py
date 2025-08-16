class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort(reverse=True)
        cnt = 0
        while amount[0] > 0:
            amount.sort(reverse=True)
            if amount[0] > 0 and amount[1] > 0:
                amount[0] -= 1
                amount[1] -= 1
                cnt += 1
            elif amount[0] > 0 and amount[1] == 0:
                amount[0] -= 1
                cnt += 1
            amount.sort(reverse=True)
        return cnt
