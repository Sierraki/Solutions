from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.a = [""] * n
        self.ptr = 0
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.a[idKey - 1] = value
        if self.a[self.ptr] == "":
            return []
        else:
            b = []
            while self.ptr < self.n and self.a[self.ptr] != "":
                b.append(self.a[self.ptr])
                self.ptr += 1
            return b


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
