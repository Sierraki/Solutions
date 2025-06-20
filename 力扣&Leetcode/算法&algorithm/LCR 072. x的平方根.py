class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(floor(sqrt(x)))


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        while ans**2 <= x:
            ans += 1
        return ans - 1
