from typing import List
from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = Counter(digits)
        ans = []
        # 枚举所有三位数偶数
        for i in range(100, 1000, 2):
            if Counter(map(int, str(i))) <= cnt:
                ans.append(i)
        return ans
