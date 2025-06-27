class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for i in range(min(len(word1), len(word2))):
            res.append(word1[i])
            res.append(word2[i])
            idx = i
        if len(word1) == len(word2):
            return "".join(res)
        else:
            if len(word1) > len(word2):
                return "".join(res) + word1[idx + 1 :]
            else:
                return "".join(res) + word2[idx + 1 :]
