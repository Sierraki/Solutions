class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = [j for i in matrix for j in i]
        if not a:
            return False
        a.sort()
        print(a)
        lc = bisect.bisect(a, target)
        return a[lc - 1] == target
