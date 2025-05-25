class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        mx = 0
        for idx, i in enumerate(strs):
            if i.isdigit():
                strs[idx] = int(i)
            else:
                strs[idx] = len(i)
            mx = max(strs[idx], mx)
        return mx
