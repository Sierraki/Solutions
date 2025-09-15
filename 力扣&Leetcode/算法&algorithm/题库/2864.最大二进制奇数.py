class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = Counter(s)
        if cnt["1"] == 1:
            return "0" * cnt["0"] + "1"
        else:
            return "1" * (cnt["1"] - 1) + "0" * cnt["0"] + "1"
