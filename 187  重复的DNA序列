from typing import List
from collections import Counter


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cnt = Counter()
        cnt[s[:10]] += 1
        for i in range(10, len(s)):
            cnt[s[i - 9 : i + 1]] += 1
        # print(cnt)
        a = [i for i, j in cnt.items() if j >= 2]
        return a
