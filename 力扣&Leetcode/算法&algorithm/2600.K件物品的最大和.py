class Solution:
    def kItemsWithMaximumSum(
        self, numOnes: int, numZeros: int, numNegOnes: int, k: int
    ) -> int:
        nums = [1] * numOnes + [0] * numZeros + [-1] * numNegOnes
        res = 0
        for i in nums:
            k -= 1
            if k < 0:
                break
            res += i
        return res
