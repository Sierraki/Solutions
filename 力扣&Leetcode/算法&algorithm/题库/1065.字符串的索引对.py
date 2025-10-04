class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []
        for i in words:
            for j in range(len(text)):
                if text[j : j + len(i)] == i:
                    res.append([j, j + len(i) - 1])
        res.sort(key=lambda x: [x[0], x[1]])
        return res
