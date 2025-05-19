class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        t = sum(cardPoints)
        wl = n - k
        s = 0
        cur = 0

        for i in range(wl):
            cur += cardPoints[i]
        s = cur

        for i in range(wl, n):

            cur = cur + cardPoints[i] - cardPoints[i - wl]
            s = min(cur, s)

        return t - s
