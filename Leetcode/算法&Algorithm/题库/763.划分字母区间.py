class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cnt = defaultdict(list)
        for i, j in enumerate(s):
            cnt[j].append(i)
        res = [[i[0], i[-1]] for i in cnt.values()]
        res.sort()
        ans = []
        while res:
            cur = res[0]
            if not ans:
                ans.append(cur)
            else:
                if cur[0] <= ans[-1][-1]:
                    ans[-1][-1] = max(ans[-1][-1], cur[1])
                else:
                    ans.append(cur)
            del res[0]
        return [j - i + 1 for i, j in ans]
