class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = [0, 0]
        for idx, i in enumerate(mat):
            if i.count(1) > res[1]:
                res = [idx, i.count(1)]
        return res
