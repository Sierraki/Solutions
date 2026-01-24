class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        def fun(a, tar) -> bool:
            if len(tar) > len(a):
                return False
            return a[: len(tar)] == tar

        res = sentence.split()
        for i in range(len(res)):
            if fun(res[i], searchWord):
                return i + 1
        return -1
