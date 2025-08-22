class Solution(object):
    def findRelativeRanks(self, score):
        res = [[i, idx] for idx, i in enumerate(score, start=1)]
        res.sort(key=lambda x: -x[0])
        for idx, i in enumerate(res):
            if idx == 0:
                ans = "Gold Medal"
            elif idx == 1:
                ans = "Silver Medal"
            elif idx == 2:
                ans = "Bronze Medal"
            else:
                ans = str(idx + 1)
            i.append(ans)
        res.sort(key=lambda x: x[1])
        return [i[2] for i in res]
