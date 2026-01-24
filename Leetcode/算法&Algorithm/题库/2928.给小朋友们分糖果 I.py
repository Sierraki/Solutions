class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def cn2(n):
            return n * (n - 1) // 2 if n > 1 else 0

        return (
            cn2(n + 2) - 3 * cn2(n - limit + 1) + 3 * cn2(n - 2 * limit)
            if limit * 3 >= n
            else 0
        )
