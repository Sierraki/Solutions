class Solution:
    def numSplits(self, s: str) -> int:
        cnt1 = Counter()
        cnt2 = Counter(s)
        ans = 0
        for i in s:
            cnt1[i] += 1
            cnt2[i] -= 1
            if cnt2[i] == 0:
                del cnt2[i]
            if len(cnt1) == len(cnt2):
                ans += 1
        return ans
