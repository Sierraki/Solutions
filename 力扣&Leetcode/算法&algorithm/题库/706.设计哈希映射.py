class MyHashMap:
    def __init__(self):
        self.data = []

    def _find(self, key):
        left, right = 0, len(self.data) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.data[mid][0] == key:
                return mid
            elif self.data[mid][0] < key:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def put(self, key: int, value: int) -> None:
        idx = self._find(key)
        if idx < len(self.data) and self.data[idx][0] == key:
            self.data[idx][1] = value
        else:
            self.data.insert(idx, [key, value])

    def get(self, key: int) -> int:
        idx = self._find(key)
        if idx < len(self.data) and self.data[idx][0] == key:
            return self.data[idx][1]
        return -1

    def remove(self, key: int) -> None:
        idx = self._find(key)
        if idx < len(self.data) and self.data[idx][0] == key:
            self.data.pop(idx)
