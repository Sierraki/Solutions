class Bank:
    def __init__(self, balance: List[int]):
        self.nums = balance
        self.n = len(balance)

    def check(self, num):
        return 1 <= num <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.check(account1) and self.check(account2):
            if self.nums[account1 - 1] >= money:
                self.nums[account2 - 1] += money
                self.nums[account1 - 1] -= money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self.check(account):
            self.nums[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.check(account):
            if self.nums[account - 1] >= money:
                self.nums[account - 1] -= money
                return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
