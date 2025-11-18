class Solution:
    @lru_cache()
    def multiply(self, A: int, B: int) -> int:
        if A == 1:
            return B
        if B == 1:
            return A
        else:
            if B >= A > 1:
                return self.multiply(A - 1, B) + B
            elif A >= B > 1:
                return self.multiply(A, B - 1) + A
