class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnt = Counter(moves)
        return cnt["D"] == cnt["U"] and cnt["R"] == cnt["L"]
