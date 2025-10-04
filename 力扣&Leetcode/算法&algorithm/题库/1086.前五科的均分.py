class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        cnt = defaultdict(list)
        for i, j in items:
            cnt[i].append(j)
        res = []
        for i, j in cnt.items():
            res.append([i, sum(sorted(j, reverse=True)[:5]) // 5])
        res.sort()
        return res
