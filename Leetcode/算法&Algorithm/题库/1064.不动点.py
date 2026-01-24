class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for idx, i in enumerate(arr):
            if idx == i:
                return idx
        return -1
