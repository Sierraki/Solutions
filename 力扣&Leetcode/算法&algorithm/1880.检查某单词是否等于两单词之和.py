class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        res1 = []
        res2 = []
        res = []
        for i in firstWord:
            res1.append(ord(i) - 97)
        for i in secondWord:
            res2.append(ord(i) - 97)
        for i in targetWord:
            res.append(ord(i) - 97)
        return int("".join(map(str, res))) == int("".join(map(str, res1))) + int(
            "".join(map(str, res2))
        )
