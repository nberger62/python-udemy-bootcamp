from Account import Account

class Customer:
    def __init__(self):
        self.checkingAccount = Account()
        self.checkingAccount.type = 'Checking'
        self.checkingAccount.balance = 50

        self.accounts = [self.checkingAccount]
