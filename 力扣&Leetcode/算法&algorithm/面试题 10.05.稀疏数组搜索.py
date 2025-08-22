class Solution:
    def findString(self, words: List[str], s: str) -> int:
        for idx, i in enumerate(words):
            if i == s:
                return idx
        return -1
