class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res0 = []
        for idx, i in enumerate(groups):
            if not res0:
                if i == 0:
                    res0.append(idx)
            else:
                if len(res0) % 2 == 1:
                    if i == 1:
                        res0.append(idx)
                else:
                    if i == 0:
                        res0.append(idx)
        res1 = []
        for idx, i in enumerate(groups):
            if not res1:
                if i == 1:
                    res1.append(idx)
            else:
                if len(res1) % 2 == 1:
                    if i == 0:
                        res1.append(idx)
                else:
                    if i == 1:
                        res1.append(idx)
        if len(res0) > len(res1):
            return [words[i] for i in res0]
        else:
            return [words[i] for i in res1]
