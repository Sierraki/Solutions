class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        cnt = Counter()
        res = Counter()
        ans = []
        for i, j in queries:
            if res[i] == 0:
                res[i] = j
                cnt[j] += 1
            else:
                cnt[res[i]] -= 1
                if cnt[res[i]] == 0:
                    del cnt[res[i]]
                res[i] = j
                cnt[j] += 1
            ans.append(len(cnt))
        return ans
