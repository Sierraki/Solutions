from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        col = []
        for i in range(len(words[0])):
            a = []
            for j in range(len(words)):
                if len(words[j]) - 1 < i:
                    a.append("")
                else:
                    a.append(words[j][i])
            res = "".join(a)
            col.append(res)
        # print(col)
        st = True
        for i in range(len(words)):
            if words[i] != col[i]:
                st = False
                break
        return st
