class Solution:
    def maxFreqSum(self, s: str) -> int:
        cnt1 = Counter(i for i in s if i in "aeiou")
        cnt2 = Counter(i for i in s if i not in "aeiou")
        cnt1["a"] += 0
        cnt2["b"] += 0
        return max(cnt1.values()) + max(cnt2.values())
