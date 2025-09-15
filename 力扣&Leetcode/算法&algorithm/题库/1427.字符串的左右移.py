class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = len(s)
        for i in shift:
            a = s + s
            if i[0] == 0:
                a = s + s
                t = i[1] % n
                s = a[t : t + n]
            else:
                t = i[1] % n
                s = a[n - t : 2 * n - t]
        return s
