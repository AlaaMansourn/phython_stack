class BankAccount:
    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate=int_rate
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount
		
    def withdraw(self, amount):
        if(self.balance>amount):
            self.balance-=amount
            return True
        else:
            return False
		
    def display_account_info(self):
        print(self.balance)


    def yield_interest(self):
        if(self.balance>0):
            self.balance=self.balance+(self.balance*self.int_rate)

if __name__ == "__main__":
    account1=BankAccount()
    account2=BankAccount()

    account1.deposit(500)
    account1.deposit(1000)
    account1.deposit(4000)

    account1.withdraw(700)
    account1.yield_interest()
    print("the user one has balance of ",account1.display_account_info())


    account2.deposit(500)
    account2.deposit(990.922)
    account2.withdraw(3000)
    account2.withdraw(897)
    account2.withdraw(800)
    account2.withdraw(1000)

    print("the user one has balance of ",account2.display_account_info())

