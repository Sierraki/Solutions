class Solution:
    def partitionString(self, s: str) -> List[str]:
        check = Counter()
        res = []
        left = 0
        for i in range(left, len(s)):
            ans = s[left : i + 1]
            if ans not in check:
                res.append(ans)
                check[ans] += 1
                left = i + 1
        return res
