class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt1 = Counter(s)
        cnt2 = Counter(t)

        for i in cnt2.keys():
            if cnt2[i] > cnt1[i]:
                return i
                break
