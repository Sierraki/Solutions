class Solution:
    def lateFee(self, daysLate: List[int]) -> int:
        ans = 0
        for i in daysLate:
            if i == 1:
                ans += 1
            elif i <= 5:
                ans += 2 * i
            else:
                ans += 3 * i
        return ans
