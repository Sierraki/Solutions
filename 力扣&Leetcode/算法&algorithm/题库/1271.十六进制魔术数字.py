class Solution:
    def toHexspeak(self, num: str) -> str:
        res = hex(int(num))[2:]
        ans = ""
        for i in res:
            if i.isalpha():
                ans += i.upper()
            elif i == "0":
                ans += "O"
            elif i == "1":
                ans += "I"
            else:
                ans += i
        for i in ans:
            if i not in "ABCDEFIO":
                return "ERROR"
        return ans
