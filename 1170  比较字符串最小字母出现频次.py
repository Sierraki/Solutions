from collections import Counter
import bisect
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        for idx, i in enumerate(words):
            a = Counter(i)
            words[idx] = a[min(a)]
        for idx, i in enumerate(queries):
            a = Counter(i)
            queries[idx] = a[min(a)]
        words.sort()
        # print(words)
        # print(queries)
        for idx, i in enumerate(queries):
            lc = bisect.bisect(words, i)
            queries[idx] = len(words) - lc
        return queries
