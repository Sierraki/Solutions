class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            columnNumber, rem = divmod(columnNumber, 26)
            res.append(chr(rem + 65))
        ans = "".join(res[::-1])
        print(ans)
        return ans
