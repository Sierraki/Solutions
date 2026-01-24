class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lnums = [0]
        rnums = [0]
        for i in nums:
            lnums.append(lnums[-1] + i)
        del lnums[-1]
        nums = nums[::-1]
        for i in nums:
            rnums.append(rnums[-1] + i)
        del rnums[-1]
        rnums = rnums[::-1]
        res = []
        for i in range(len(lnums)):
            res.append(abs(lnums[i] - rnums[i]))
        return res
