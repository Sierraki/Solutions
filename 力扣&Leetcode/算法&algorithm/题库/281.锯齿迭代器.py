class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.res = []
        p1 = p2 = 0
        while p1 < len(v1) and p2 < len(v2):
            self.res.append(v1[p1])
            self.res.append(v2[p2])
            p1 += 1
            p2 += 1
        if p1 == len(v1):
            self.res += v2[p2:]
        else:
            self.res += v1[p1:]
        self.pin = 0

    def next(self) -> int:
        self.pin += 1
        return self.res[self.pin - 1]

    def hasNext(self) -> bool:
        return self.pin < len(self.res)


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
