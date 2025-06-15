class Solution:
    def generateTag(self, caption: str) -> str:
        caption = [i for i in caption]
        for idx, i in enumerate(caption):
            if i.isalpha():
                caption[idx] = i.lower()
        caption = "".join(caption)
        res = caption.split()
        def fun(word: str):
            p1 = word[:1]
            p2 = word[1:]
            a = p1.upper()
            return a + p2
        for idx, i in enumerate(res):
            res[idx] = fun(i)
        res = "".join(res)
        p1 = res[:1]
        p2 = res[1:]
        a = p1.lower()
        res = "#" + a + p2
        if len(res)>100:
            return res[:100]
        return res