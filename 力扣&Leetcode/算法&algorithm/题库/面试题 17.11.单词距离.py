class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        cnt = defaultdict(list)
        for i, j in enumerate(words):
            if j == word1:
                cnt["p1"].append(i)
            if j == word2:
                cnt["p2"].append(i)
        pin1 = pin2 = 0
        mx = float("inf")
        while pin1 < len(cnt["p1"]) and pin2 < len(cnt["p2"]):
            mx = min(mx, abs(cnt["p1"][pin1] - cnt["p2"][pin2]))
            if cnt["p1"][pin1] > cnt["p2"][pin2]:
                pin2 += 1
            elif cnt["p1"][pin1] < cnt["p2"][pin2]:
                pin1 += 1
            else:
                pin1 += 1
                pin2 += 1
        return mx
