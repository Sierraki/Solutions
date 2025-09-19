class Solution:
    def betterCompression(self, compressed: str) -> str:
        ans = ""
        res = []
        cnt = Counter()
        for i in compressed:
            if i.isalpha():
                if res:
                    cnt[tar] += int("".join(res))
                    res.clear()
                tar = i
            else:
                res.append(i)
        cnt[tar] += int("".join(res))
        key = [i for i in cnt.keys()]
        key.sort()
        for i in key:
            ans += f"{i}{str(cnt[i])}"
        return ans
