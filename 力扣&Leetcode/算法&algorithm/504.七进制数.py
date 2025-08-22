class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if abs(num) < 7:
            return str(num)
        nums = num
        res = ""
        num = abs(num)
        while num > 0:
            ans = num % 7
            num = num // 7
            res += str(ans)
        res1 = int(res[::-1])
        if nums < 0:
            res1 *= -1
        return str(res1)
