class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ["" for _ in range(numRows)]
        pin = 0
        swap = True
        for i in s:
            if swap == True:
                res[pin] += i
                pin += 1
                if pin == len(res) - 1:
                    swap = False
            else:
                res[pin] += i
                pin -= 1
                if pin == 0:
                    swap = True
        return "".join(res)
