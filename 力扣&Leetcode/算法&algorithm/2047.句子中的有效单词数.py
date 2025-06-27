class Solution:
    def countValidWords(self, sentence: str) -> int:

        def check(s: str):
            a = ",.!"
            cnt = Counter(s)
            # 不能含有数字
            for i in cnt.keys():
                if i.isdigit():
                    return False
            if cnt["-"] > 1:
                return False
            if cnt["-"] == 1:
                lc = s.index("-")
                p1 = s[:lc]
                p2 = s[lc:]
                c1 = c2 = 0
                for i in p1:
                    if i.isalpha():
                        c1 += 1
                        break
                for i in p2:
                    if i.isalpha():
                        c2 += 1
                        break
                if not (c1 > 0 and c2 > 0):
                    return False

            if len(s) == 1 and (s[0] in a or s[0].isalpha()):
                return True
            # 第一个字母不能为-。，！
            # 最后一个字母不能为-
            for idx, i in enumerate(s):
                if idx == 0:
                    if not i.isalpha():
                        return False
                elif 1 <= idx < len(s) - 1:
                    if not (i.isalpha or i == "-"):
                        return False
                    if i in a:
                        return False
                elif idx == len(s) - 1:
                    if not (i.isalpha() or i in a):
                        return False
            return True

        cnt = 0
        for i in sentence.split():
            if check(i):
                cnt += 1
        return cnt
