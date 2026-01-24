class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        tar = (sum(array1) - sum(array2)) / 2
        cnt = set(array2)
        res = []
        for i in set(array1):
            if i - tar in cnt:
                res = [i, i - tar]
                break
        return res
