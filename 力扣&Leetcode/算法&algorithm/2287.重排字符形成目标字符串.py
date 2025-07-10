class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        cnt1 = Counter()
        cnt2 = Counter(target)
        for i in s:
            if i in target:
                cnt1[i] += 1
        if len(cnt1) < len(cnt2):
            return 0
        else:
            ans = float("inf")
            for i, j in cnt1.items():
                if cnt1[i] >= cnt2[i]:
                    ans = min(ans, cnt1[i] // cnt2[i])
                else:
                    return 0
        return ans
