class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt = 0
        for i, j, k in items:
            if ruleKey == "type":
                tar = i
            elif ruleKey == "color":
                tar = j
            else:
                tar = k
            if tar == ruleValue:
                cnt += 1
        return cnt
