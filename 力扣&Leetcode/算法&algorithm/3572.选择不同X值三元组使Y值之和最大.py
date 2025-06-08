class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        a = list(zip(y, x))
        a.sort(reverse=True)
        l = m = r = 0
        while a[l][1] == a[m][1] or a[l][1] == a[r][1] or a[r][1] == a[m][1]:
            if a[l][1] == a[r][1] or a[m][1] == a[r][1]:
                r += 1
            if a[l][1] == a[m][1]:
                m += 1
            if r > len(x) - 1:
                return -1
            if a[l][1] != a[m][1] and a[l][1] != a[r][1] and a[r][1] != a[m][1]:
                break
        res = a[l][0] + a[m][0] + a[r][0]
        return res
