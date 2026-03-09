class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = list(range(1, n + 1))
        tar = k - 1
        while len(res) > 1:
            del res[tar]
            left = len(res) - tar
            left1 = k - left
            res1 = left1 % len(res)
            if res1 > 0:
                res1 -= 1
            else:
                res1 = len(res) - 1
            tar = res1
        return res[0]