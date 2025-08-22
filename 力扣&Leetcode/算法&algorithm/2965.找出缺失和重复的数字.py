class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) ** 2
        cnt = Counter()
        su = 0
        for i in grid:
            for j in i:
                su += j
                if j not in cnt:
                    cnt[j] += 1
                else:
                    a = j
        su -= a
        b = (1 + n) * n // 2 - su
        return [a, b]
