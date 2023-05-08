from account import Account


class CurrentAccount(Account):
    def _init_(self):
        Account.__init__(self)


current = CurrentAccount()
current.deposit(500)
current.withdrawal(50)
print(current.Account_balance)
