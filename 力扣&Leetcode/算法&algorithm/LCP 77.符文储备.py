class Solution:
    def runeReserve(self, runes: List[int]) -> int:
        if len(runes) == 1:
            return 1
        runes.sort()
        cnt = 1
        mx = 0
        for i in range(1, len(runes)):
            if abs(runes[i] - runes[i - 1]) <= 1:
                cnt += 1
            else:
                cnt = 1
            mx = max(mx, cnt)
        return mx
