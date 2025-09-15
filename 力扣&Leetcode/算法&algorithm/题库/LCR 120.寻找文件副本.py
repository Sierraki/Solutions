class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        cnt = Counter(documents)
        for i, j in cnt.items():
            if j > 1:
                return i
