class Logger:

    def __init__(self):
        self.cnt = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.cnt:
            self.cnt[message] = timestamp + 10
            return True
        else:
            if timestamp >= self.cnt[message]:
                self.cnt[message] = timestamp + 10
                return True
            else:
                return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
