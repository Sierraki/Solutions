class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = Counter(s)
        ans = ""
        for i in order:
            ans += i * cnt[i]
            del cnt[i]
        for i, j in cnt.items():
            ans += i * j
        return ans
