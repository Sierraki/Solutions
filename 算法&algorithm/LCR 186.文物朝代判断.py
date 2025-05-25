class Solution:
    def checkDynasty(self, places: List[int]) -> bool:
        mx = -1
        mi = 14
        cnt = Counter(places)
        del cnt[0]
        for i in places:
            mx = max(mx, i)
        for i in places:
            if i == 0:
                continue
            else:
                mi = min(mi, i)
        return mx - mi <= 4 and max(cnt.values()) <= 1
