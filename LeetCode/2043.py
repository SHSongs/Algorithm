from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        account1 -= 1
        account2 -= 1
        if account1 < len(self.balance) and account2 < len(self.balance):
            if self.balance[account1] >= money:
                self.balance[account1] -= money
                self.balance[account2] += money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        account -= 1
        if account < len(self.balance):
            self.balance[account] += money
            return True

        return False

    def withdraw(self, account: int, money: int) -> bool:
        account -= 1
        if account < len(self.balance):
            if self.balance[account] - money >= 0:
                self.balance[account] = self.balance[account] - money
                return True

        return False


# Your Bank object will be instantiated and called as such:
obj = Bank([10, 100, 20, 50, 30])
param_1 = obj.transfer(5, 1, 20)
print(param_1)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
