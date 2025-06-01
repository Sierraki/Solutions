class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        cnt = Counter()
        for i in orders:
            cnt[i[2]] += 1
        title = [i for i in cnt.keys()]
        title.sort()
        cnt2 = defaultdict(list)
        for i in orders:
            cnt2[i[1]].append(i[2])
        # count
        cnt3 = defaultdict(Counter)
        for i, j in cnt2.items():
            cnt3[i].update(j)
        # table list
        table = [int(i[1]) for i in orders]
        table = sorted(list(set(table)))
        table = [str(i) for i in table]
        ans = []
        for i in table:  # table num
            res = []
            res.append(i)
            for j in title:  # food name
                if j in cnt3[str(i)]:
                    res.append(str(cnt3[str(i)][j]))
                else:
                    res.append("0")
            ans.append(res)
        title = ["Table"] + title
        ans.insert(0, title)
        return ans
