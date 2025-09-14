class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s = 0
        mi = float("inf")
        for i in nums:
            s += i
            mi = min(s, mi)
        print(mi)
        if mi < 0:
            return 1 - mi
        else:
            return 1
