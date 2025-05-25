class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = [j for i in matrix for j in i]
        if not a:
            print(False)
        a.sort()
        print(a)
        lc = bisect.bisect_left(a, target)
        lc1 = bisect.bisect(a, target)
        return a[lc1 - 1] == target or a[lc - 1] == target
