class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if k % 2:
            return str(k // 2 % 2)
        k //= k & -k
        return str(1 - k // 2 % 2)
