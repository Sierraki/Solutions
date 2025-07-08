class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = -float("inf")
        for i in range(2, len(num)):
            a = num[i - 2 : i + 1]
            if num[i] == num[i - 1] == num[i - 2]:
                ans = max(ans, int(a))
        if ans == -float("inf"):
            return ""
        if ans == 0:
            return "000"
        return str(ans)
