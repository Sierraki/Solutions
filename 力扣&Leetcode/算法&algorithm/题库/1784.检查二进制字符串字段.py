class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        cnt = Counter(s)
        if cnt["1"] > 0 and cnt["0"] == 0 or (cnt["0"] > 0 and cnt["1"] == 0):
            return True
        for idx, i in enumerate(s):
            if i == "0":
                lc = idx
                break
        p = s[lc:]
        return Counter(p)["1"] <= 0
