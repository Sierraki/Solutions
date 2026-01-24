class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        tar = Counter("balloon")
        ans = float("inf")
        for i, j in tar.items():
            if i in cnt:
                if cnt[i] >= j:
                    ans = min(ans, cnt[i] // j)
                else:
                    return 0
            else:
                return 0
        return ans
