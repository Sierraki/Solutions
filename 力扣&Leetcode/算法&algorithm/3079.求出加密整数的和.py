class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(x: int) -> int:
            cnt = len(str(x))
            tar = max(map(int, str(x)))
            res = int(str(tar) * cnt)
            return res

        res = 0
        for i in nums:
            res += encrypt(i)
        return res
