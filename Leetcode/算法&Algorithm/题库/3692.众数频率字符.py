class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        cnt = Counter(s)
        res = defaultdict(set)
        len_fre = Counter()
        max_len = 0
        for i, j in cnt.items():
            res[j].add(i)
            max_len = max(len(res[j]), max_len)
        for i in res.values():
            len_fre[len(i)] += 1
        res1 = [[i, j] for i, j in res.items() if len(j) == max_len]
        mx = 0
        for i, j in res1:
            if i > mx:
                mx = i
                ans = j
        return "".join(ans)
