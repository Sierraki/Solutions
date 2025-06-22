class Solution:
    def sortString(self, s: str) -> str:
        cnt = Counter(s)
        res = [[i, j] for i, j in cnt.items()]
        res.sort()
        ans = []
        while res:
            # ---->
            l = 0
            while l < len(res):
                if res[l][1] > 0:
                    ans.append(res[l][0])
                    res[l][1] -= 1
                    if res[l][1] == 0:
                        del res[l]
                    else:
                        l += 1
            # <----
            r = -1
            while r >= -len(res):
                if res[r][1] > 0:
                    ans.append(res[r][0])
                    res[r][1] -= 1
                    if res[r][1] == 0:
                        del res[r]
                    else:
                        r -= 1
        return "".join(ans)
