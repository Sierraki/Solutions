class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumodd = ((n * 2 + 1) * n - n) // 2
        sumeven = sumodd + n
        ans = 0
        for i in range(1, floor(sqrt(sumodd)) + 1):
            if sumeven % i == 0 and sumodd % i == 0:
                ans = i
        return ans
