class MyHashSet:

    def __init__(self):
        self.a = set()

    def add(self, key: int) -> None:
        self.a.add(key)

    def remove(self, key: int) -> None:
        if key in self.a:
            self.a.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.a


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


class MyHashSet:

    def __init__(self):
        self.set = [False] * 1000001

    def add(self, key):
        self.set[key] = True

    def remove(self, key):
        self.set[key] = False

    def contains(self, key):
        return self.set[key]


# 时间复杂度 O1
