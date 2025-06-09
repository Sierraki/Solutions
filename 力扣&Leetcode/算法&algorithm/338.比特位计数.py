class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            ans = bin(i)[2::]
            cnt = ans.count("1")
            res.append(cnt)
        return res
