class CustomStack:

    def __init__(self, maxSize: int):
        self.s = []
        self.maxSize = maxSize
        self.n = 0

    def push(self, x: int) -> None:
        if self.n < self.maxSize:
            self.s.append(x)
            self.n += 1

    def pop(self) -> int:
        ans = -1
        if self.s:
            ans = self.s[-1]
            self.s.pop()
            self.n -= 1
        return ans

    def increment(self, k: int, val: int) -> None:
        if not self.s:
            return self.s
        else:
            if k > self.n:
                for i in range(self.n):
                    self.s[i] += val
            else:
                for i in range(k):
                    self.s[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


class CustomStack:

    def __init__(self, maxSize: int):
        self.s = [0] * maxSize
        self.n = -1

    def push(self, x: int) -> None:
        if self.n < len(self.s) - 1:
            self.n += 1
            self.s[self.n] = x

    def pop(self) -> int:
        ans = -1
        if self.n > -1:
            ans = self.s[self.n]
            self.n -= 1
        return ans

    def increment(self, k: int, val: int) -> None:
        if self.n <= -1:
            return []
        else:
            if k - 1 > self.n:
                for i in range(self.n + 1):
                    self.s[i] += val
            else:
                for i in range(k):
                    self.s[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

