class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        def fun(a: list) -> int:
            for i in range(len(a)):
                if a[i] != a[len(a) - 1]:
                    return len(a) - 1 - i

        return max(fun(colors), fun(colors[::-1]))
