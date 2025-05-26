class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt1 = Counter(s1)
        cnt2 = Counter(s2)
        if cnt1 != cnt2:
            return False
        else:
            if s1 == s2:
                return True
            else:
                cnt = defaultdict(int)
                n = len(s1)
                for i in range(n):
                    if s1[i] != s2[i]:
                        res = tuple(sorted([s1[i], s2[i]]))
                        cnt[res] += 1
                if len(cnt) > 1 or max(cnt.values()) > 2:
                    return False
                else:
                    return True
