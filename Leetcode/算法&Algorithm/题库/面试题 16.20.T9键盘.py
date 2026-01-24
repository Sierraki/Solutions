class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        cnt = {
            "a": 2,
            "b": 2,
            "c": 2,  # 2
            "d": 3,
            "e": 3,
            "f": 3,  # 3
            "g": 4,
            "h": 4,
            "i": 4,  # 4
            "j": 5,
            "k": 5,
            "l": 5,  # 5
            "m": 6,
            "n": 6,
            "o": 6,  # 6
            "p": 7,
            "q": 7,
            "r": 7,
            "s": 7,  # 7
            "t": 8,
            "u": 8,
            "v": 8,  # 8
            "w": 9,
            "x": 9,
            "y": 9,
            "z": 9,  # 9
        }
        res = []
        for i in words:
            if len(i) == len(num):
                p1 = p2 = 0
                while p1 == p2 and p1 < len(num):
                    if num[p1] == str(cnt[i[p2]]):
                        if p1 == p2 == len(num) - 1:
                            res.append(i)
                        p1 += 1
                        p2 += 1
                        continue
                    else:
                        break
        return res
