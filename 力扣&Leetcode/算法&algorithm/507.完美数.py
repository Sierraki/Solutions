class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        res = set()
        for i in range(1, int(sqrt(num)) + 1):
            if num % i == 0:
                res.add(i)
                res.add(num // i)
        return num == sum(res) - num
