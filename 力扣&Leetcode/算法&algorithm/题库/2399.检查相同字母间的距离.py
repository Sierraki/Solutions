class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        al = "abcdefghijklmnopqrstuvwxyz"
        cn = dict(zip(al, distance))
        cnt = defaultdict(list)
        for idx, i in enumerate(s):
            cnt[i].append(idx)
        res = Counter()
        for i, j in cnt.items():
            if len(j) == 2:
                res[i] = abs(j[0] - j[1]) - 1
        for i in res.keys():
            if res[i] != cn[i]:
                return False
        return True
