class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        st = False
        a = []
        n = len(s)
        for i in words:
            a.append(i)
            b = "".join(a)
            if s in b and n == len(b):
                st = True
                break
            if len(b) > n:
                break
        return st
