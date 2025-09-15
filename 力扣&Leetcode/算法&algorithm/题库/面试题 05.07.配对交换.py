class Solution:
    def exchangeBits(self, num: int) -> int:
        res1 = [i for i in bin(num)[2:]]
        if len(res1) % 2 == 1:
            res1.insert(0, "0")
        for i in range(1, len(res1), 2):
            res1[i - 1], res1[i] = res1[i], res1[i - 1]
        ans = "".join(res1)
        return int(ans, 2)
