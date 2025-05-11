from typing import List
from collections import Counter


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        cnt = Counter()
        for a in range(len(emails)):
            co = emails[a]
            # 切片@后面的
            lc = co.index("@")  # @ location
            p2 = co[lc:]  # after @ include @
            p1 = co[:lc]  # before @ not include @
            # print(p1)
            # remove after+
            if p1.count("+") > 0:
                lc1 = p1.index("+")  # + location
                p1 = p1[:lc1]
            # remove .
            if p1.count(".") > 0:
                p1 = p1.replace(".", "")
            co = p1 + p2
            cnt[co] += 1
        return len(cnt)
