class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        cnt = 0
        res = 0
        for i in weight:
            res += i
            if res <= 5000:
                cnt += 1
            else:
                return cnt
        return cnt
