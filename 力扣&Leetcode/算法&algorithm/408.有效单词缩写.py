class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        res = []
        swap = False
        for i in abbr:
            if i.isalpha():
                swap = True
        if not swap:
            if abbr[0] != "0":
                return len(word) == int(abbr)
            else:
                return False
        num = []
        for idx, i in enumerate(abbr):
            if num and (i.isalpha()):
                if num[0] == "0":
                    return False
                res.append(("".join(num)))
                num = []
            if i.isdigit():
                num.append(i)
            elif i.isalpha():
                res.append(i)
            if num and idx == len(abbr) - 1:
                if num[0] == "0":
                    return False
                res.append(("".join(num)))
        # return(res)
        tar = []
        idx = 0
        for idxx, i in enumerate(res):
            if i.isalpha():
                tar.append([i, idx])
                idx += 1
            elif i.isdigit():
                idx += int(i)
            if idxx == len(res) - 1 and res[-1].isdigit():
                tar.append([word[-1], idx - 1])
        # return(tar)
        for i, j in tar:
            if j >= len(word) or word[j] != i:
                return False
        if tar[-1][-1] == len(word) - 1:
            return True
        return False
