from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        # print(cnt)
        a = []
        for i in cnt.values():
            a.append(i)
        return len(set(a)) == len(a)
