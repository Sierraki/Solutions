class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for idx, i in enumerate(words):
            if x in i:
                res.append(idx)
        return res
