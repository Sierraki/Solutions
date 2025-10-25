class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # 在满足这么多位情况下可以写多少个9
        sum1 = sum
        ans = ""
        res = [0] * num
        if num * 9 > sum1:
            ans = ""
        for i in range(len(res)):
            if sum1 >= 9:
                res[i] = 9
                sum1 -= 9
            elif sum1 > 0:
                res[i] = sum1
                break
        aa = 0
        for i in res:
            aa += i
        if aa == sum:
            return "".join(map(str, res))
        return ""