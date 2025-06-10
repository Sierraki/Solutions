class Solution:
    def convertDateToBinary(self, date: str) -> str:
        res = date.split("-")
        for i in range(len(res)):
            res[i] = bin(int(res[i]))[2:] + "-"
        ans = "".join(res)
        return ans[:-1]
