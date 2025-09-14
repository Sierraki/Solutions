class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        mx = 0
        for i in sentences:
            a = []
            a.extend(i.split(" "))
            mx = max(mx, len(a))
        return mx
