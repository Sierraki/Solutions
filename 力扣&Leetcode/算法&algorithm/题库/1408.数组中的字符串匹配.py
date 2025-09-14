class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len, reverse=True)
        a = []
        b = []
        for i in words:
            if i not in a:
                a.append(i)
            for j in a:
                if i in j and i != j:
                    b.append(i)
        return list(set(b))
