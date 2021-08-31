class BankAccount:

    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate = int_rate
    def deposit(self, amount):
        self.balance+= amount
        return self
    def withdraw(self, amount):
        if(amount < self.balance): 
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -=5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if(self.balance > 0):
            self.balance *= self.int_rate
        return self

account1 = BankAccount(1.1, 1000)
account2 = BankAccount(1.1, 200)

account1.deposit(100).deposit(1000).deposit(200).withdraw(400).yield_interest().display_account_info()
account2.deposit(2000).deposit(3000).withdraw(200).withdraw(1000).withdraw(100).withdraw(300).yield_interest().display_account_info()

