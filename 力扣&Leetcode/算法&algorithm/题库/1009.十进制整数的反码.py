class Solution:
    def bitwiseComplement(self, n: int) -> int:
        res = bin(n)[2:]
        ans = ""
        for i in res:
            if i == "1":
                ans += "0"
            else:
                ans += "1"
        return int(ans, 2)
