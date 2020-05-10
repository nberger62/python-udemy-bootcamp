

# Defining Account Test Data
from Account import Account
from Customer import Customer

account = Account()
account.balance = 500
accountTwo = Account()
accountTwo.balance = 700
accounts = [account, accountTwo]

customer = Customer()

highestAccount = Account()
for a in accounts:
    if a.balance > highestAccount.balance:
        highestAccount = a
        print("Account Balance: " + str(a.balance))

print('Account with the most balance: ' + str(highestAccount.balance)
print('My first customer's balance: ' + str(customer.accounts.balance)
print('My first customer's type: ' + str(customer.accounts.type)