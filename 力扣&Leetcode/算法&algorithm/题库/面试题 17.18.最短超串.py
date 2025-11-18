class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        goal = set(small)
        cnt = Counter()
        cur = set()
        res = []
        l = 0
        for i, j in enumerate(big):
            if j in goal:
                cnt[j] += 1
                cur.add(j)
            while cur == goal and l <= i:
                res.append([l, i])
                cnt[big[l]] -= 1
                if cnt[big[l]] == 0:
                    del cnt[big[l]]
                    cur.remove(big[l])
                l += 1
        mi = float("inf")
        for i, j in res:
            mi = min(mi, j - i)

        ans = [[i, j] for i, j in res if j - i == mi]
        if ans:
            return ans[0]
        return []
