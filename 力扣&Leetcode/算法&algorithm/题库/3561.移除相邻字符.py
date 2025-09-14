class Solution:
    def resultingString(self, s: str) -> str:
        def check(i, j):
            return abs(ord(i) - ord(j)) == 1 or {i, j} == {"a", "z"}

        a = []
        for i in s:
            if a != [] and check(a[-1], i):
                a.pop()
            else:
                a.append(i)
        return "".join(a)
