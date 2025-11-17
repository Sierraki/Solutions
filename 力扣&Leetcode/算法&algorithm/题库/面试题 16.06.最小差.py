class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        ans = float("inf")
        p1 = p2 = 0
        while p1 < len(a) and p2 < len(b):
            ans = min(ans, abs(a[p1] - b[p2]))
            if a[p1] > b[p2]:
                p2 += 1
            elif a[p1] < b[p2]:
                p1 += 1
            else:
                return 0
        return ans
