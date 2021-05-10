class User:
    def __init__(self,name): #this is the constructor
        
        self.name=name
        self.account=BankAccount()


    def make_withdrawal(self,amount): #this is the method 1
        
        self.account.withdraw(amount)
    
    def make_deposit(self,amount):
        self.account.deposit(amount)
    


    
    def display_user_balance(self): 
        
       
        print("balance" , self.account.display_account_info(),"name",self.name)

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

    user1=User('alaa')
    user1.make_deposit(5000)
    user1.make_withdrawal(200)
    user1.display_user_balance()

    
    