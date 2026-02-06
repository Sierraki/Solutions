class Solution:
    def countMonobit(self, n: int) -> int:
        ans = 1
        k = 1
        while True:
            cur = (1 << k) - 1
            if cur > n:
                break
            ans += 1
            k += 1
        return ans
