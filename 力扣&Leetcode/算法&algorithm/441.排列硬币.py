class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((-1 + floor(sqrt(1 + 8 * n))) // 2)
