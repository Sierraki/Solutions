from typing import List
from collections import defaultdict


class Solution:
    def mergeSimilarItems(
        self, items1: List[List[int]], items2: List[List[int]]
    ) -> List[List[int]]:
        cnt = defaultdict()
        items1 += items2
        for i in items1:
            if i[0] not in cnt:
                cnt[i[0]] = 0
        # print(cnt)
        for i in items1:
            cnt[i[0]] += i[1]
        # print(cnt)
        a = [[i, j] for i, j in cnt.items()]
        a.sort()
        return a
