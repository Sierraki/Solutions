class Solution:
    def minimumSum(self, num: int) -> int:
        a = [i for i in str(num)]
        a.sort()
        b = [a[0], a[2]]
        c = [a[1], a[3]]

        b = int("".join(b))
        c = int("".join(c))
        return b + c
