from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        last = 0
        mx = 0
        n = len(forts)
        for i in range(n):
            if forts[i] != 0 and forts[last] == 0:
                last = i
            elif forts[i] == forts[last]:
                last = i
            else:
                if forts[i] == 1 and forts[last] == -1:
                    mx = max(mx, i - last - 1)
                    last = i
                if forts[i] == -1 and forts[last] == 1:
                    mx = max(mx, i - last - 1)
                    last = i
        return mx
