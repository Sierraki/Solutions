class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = sorted([j for i in matrix for j in i])
        lc = bisect.bisect_left(a, target)
        lc1 = bisect.bisect(a, target)
        return a[lc1 - 1] == target or a[lc - 1] == target
