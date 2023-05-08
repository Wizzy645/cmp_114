from account import Account
class SavingsAccount(Account):
    def __init__(self, balance):
        Account.__init__(self)
        self.limit = 10000

    def withdraw(self, amount):
        if amount > self.limit:
            print("Insufficient funds")
        else:
            self.Account_balance -= amount


account = SavingsAccount(1000)
print(account.Account_balance)

account.deposit(500)
print(account.Account_balance)

account.withdraw(200)
print(account.Account_balance)

account.withdraw(1500)
print(account.Account_balance)
