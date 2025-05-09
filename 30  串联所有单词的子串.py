from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words[0])  # 单个单词长度
        k = len(words) * n  # 窗口长度
        target = Counter(words)  # 对照目标
        left, right = 0, k - 1
        ans = []  # 答案列表
        while right < len(s):
            tmp = []  # 临时表 
            for i in range(left, right + 1, n):
                tmp.append(s[i : i + n])
            if Counter(tmp) == target:
                ans.append(left)
            left += 1
            right += 1
        return ans
