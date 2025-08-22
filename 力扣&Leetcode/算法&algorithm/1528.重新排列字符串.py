class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = dict(zip(indices, s))
        ans = ""
        for i in range(len(indices)):
            ans += res[i]
        return ans
