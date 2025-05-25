class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort(reverse=True)
        a = [i for i in range(1, n + 1)]
        res = 0
        for i in range(n):
            if i == n - 1 and citations[i] > a[i]:
                res = a[i]
                break
            elif a[i] > citations[i]:
                res = a[i] - 1
                break
            elif a[i] == citations[i]:
                res = a[i]
                break
        return res
