class StringIterator:

    def __init__(self, compressedString: str):
        words = re.findall(r"[A-Za-z]", compressedString)
        nums = list(map(int, re.findall(r"\d+", compressedString)))
        self.res = list(zip(words, nums))
        self.pin = 0  # 当前指向哪个字母
        self.cnt = 0  # 当前字母已经弹出的次数

    def next(self) -> str:
        if not self.hasNext():
            return " "
        ch, total = self.res[self.pin]
        self.cnt += 1
        if self.cnt == total:
            self.pin += 1
            self.cnt = 0
        return ch

    def hasNext(self) -> bool:
        return self.pin < len(self.res)


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
