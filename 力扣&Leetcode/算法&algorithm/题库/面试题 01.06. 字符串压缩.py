class Solution:
    def compressString(self, S: str) -> str:
        left = 0
        res = []
        for idx, i in enumerate(S):
            if idx == len(S) - 1 and S[left] == i:
                res.append(S[left])
                res.append(idx - left + 1)
            if i != S[left]:
                res.append(S[left])
                res.append(idx - left)
                left = idx
                if left == len(S) - 1:
                    res.append(S[left])
                    res.append(idx - left + 1)
        ans = "".join(map(str, res))
        if len(ans) < len(S):
            return ans
        return S
