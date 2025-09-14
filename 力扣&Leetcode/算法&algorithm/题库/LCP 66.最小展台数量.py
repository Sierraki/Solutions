class Solution:
    def minNumBooths(self, demand: List[str]) -> int:
        cnt = Counter()
        for i in demand:
            cnt1 = Counter(i)
            for j in i:
                cnt[j] = max(cnt[j], cnt1[j])
        return sum(cnt.values())
