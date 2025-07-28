class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        cnt = Counter("".join(words))
        for i in cnt.values():
            if i % n != 0:
                return False
        return True
