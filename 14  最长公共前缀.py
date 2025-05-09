from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                ans.append(strs[0][i])
            else:
                break
        ans = "".join(ans)
        return ans
