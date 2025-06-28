class Solution:
    def secondHighest(self, s: str) -> int:
        res = set()
        for i in s:
            if i.isdigit():
                res.add(int(i))
        res = sorted(list(res), reverse=True)
        if len(res) < 2:
            return -1
        return res[1]
