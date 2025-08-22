class Solution:
    def greatestLetter(self, s: str) -> str:
        cnt = defaultdict(list)
        for i in s:
            cnt[i.lower()].append(i)
        res = []
        for i in cnt.values():
            if len(set(i)) >= 2:
                res.append(i[0].upper())
        res.sort()
        if not res:
            return ""
        return res[-1]
