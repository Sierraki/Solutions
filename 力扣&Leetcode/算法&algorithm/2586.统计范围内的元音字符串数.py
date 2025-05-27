class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        words = words[left : right + 1]
        target = ["a", "e", "i", "o", "u"]
        cnt = 0
        for i in words:
            if i[0] in target and i[-1] in target:
                cnt += 1
        return cnt
