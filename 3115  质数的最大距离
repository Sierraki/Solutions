class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        a = []
        for idx, i in enumerate(nums):
            s = True
            if i == 1:
                s = False
            else:
                for j in range(2, i):
                    if i % j == 0:
                        s = False
                        break
            if s == True:
                a.append(idx)
        a.sort()
        return abs(a[-1] - a[0])
