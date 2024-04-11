class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Account:
    def __init__(self, account_number, balance, owner):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.owner.username}")
        print(f"Current Balance: {self.balance} INR")


class Transaction:
    def __init__(self, from_account, to_account, amount):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount

    def process(self):
        if self.from_account.balance >= self.amount:
            self.from_account.withdraw(self.amount)
            self.to_account.deposit(self.amount)
            print("Transaction successful", )
        else:
            print("Transaction failed: Insufficient funds")

class Bank:
    def __init__(self):
        self.users = {}
        self.accounts = {}

    def create_user(self, username, password):
        if username not in self.users:
            self.users[username] = User(username, password)
            return True
        else:
            print("Username already exists")
            return False

    def create_account(self, username, account_number, balance):
        if username in self.users:
            user = self.users[username]
            account = Account(account_number, balance, user)
            self.accounts[account_number] = account
            return True
        else:
            print("User does not exist")
            return False




bank = Bank()

# Create users and accounts
bank.create_user("john_doe", "password123")
bank.create_account("john_doe", "1234567890", 54000)
bank.create_user("jane_smith", "qwerty456") 
bank.create_account("jane_smith", "9876543210", 21500)

# Get the account objects
john_account = bank.accounts["1234567890"]
jane_account = bank.accounts["9876543210"]

# Perform transactions
transaction1 = Transaction(john_account, jane_account, 10700)
transaction1.process()

transaction2 = Transaction(jane_account, john_account, 5080)
transaction2.process()

transaction3 = Transaction(john_account, jane_account, 20900)
transaction3.process()

print("\nUpdated Balances:")
john_account.display_balance()
jane_account.display_balance()