class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        ans = 1
        mx = 1
        if k % 2 == 0 or k % 5 == 0:
            return -1
        else:
            while ans % k != 0:
                ans = ans * 10 + 1
                mx += 1
        return mx
