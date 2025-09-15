class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        cnt1 = {s1[0], s1[2]}
        cnt2 = {s1[1], s1[3]}
        cnt3 = {s2[0], s2[2]}
        cnt4 = {s2[1], s2[3]}
        return cnt1 == cnt3 and cnt2 == cnt4
