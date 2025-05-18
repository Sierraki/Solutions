class TwoSum:

    def __init__(self):
        self.l1 = []

    def add(self, number: int) -> None:
        self.l1.append(number)

        return self.l1

    def find(self, value: int) -> bool:
        seen = set()
        if not self.l1:  # 如果列表为空，直接返回 False
            return False
        for num in self.l1:
            complement = value - num  # 计算补数
            if complement in seen:  # 检查补数是否在哈希表中
                return True
            seen.add(num)
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
