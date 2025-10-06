class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        num = str(n)
        le = len(num)
        res = []
        for i in range(len(num)):
            ans = num[i] + "0" * (le - 1)
            le -= 1
            if int(ans) != 0:
                res.append(int(ans))
        return res
