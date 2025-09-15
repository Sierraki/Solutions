class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt = Counter(words1 + words2)
        res1 = {i: j for i, j in cnt.items() if j == 2}
        res2 = {i: j for i, j in Counter(words1).items() if j == 1}
        return sum([1 for i in res1 if i in res2])
