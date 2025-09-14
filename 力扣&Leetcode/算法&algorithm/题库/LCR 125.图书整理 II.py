class CQueue:

    def __init__(self):
        self.a = []

    def appendTail(self, value: int) -> None:
        self.a.append(value)

    def deleteHead(self) -> int:
        if self.a:
            book = self.a[0]
            del self.a[0]
            return book
        else:
            return -1


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
