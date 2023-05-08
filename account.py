class Account:

    def __init__(self):
        self.name = "Adesina Olamide"
        self.Account_number = 7047310272
        self.Account_balance = 10000

    def deposit(self, amount):
        var = self.Account_balance + amount
        print("deposit_successful")

    def withdrawal(self, amount):
        self.Account_balance = self.Account_balance - amount
        print("withdrawal_successful")
