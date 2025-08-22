class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        l = False
        res = set()
        for idx, i in enumerate(word):
            if idx == len(word) - 1 and l == False and i.isdigit():
                ans = int(i)
                res.add(int(ans))
            elif l == False and i.isdigit():
                left = idx
                l = True

            elif l == True:
                if i.isalpha():
                    right = idx
                    ans = word[left:right]
                    l = False
                    res.add(int(ans))
                if i.isdigit() and idx == len(word) - 1:
                    right = idx
                    ans = word[left:]
                    l = False
                    res.add(int(ans))
        return len(res)
