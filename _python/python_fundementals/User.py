class User:
    def __init__(self,balance=0,name): #this is the constructor
        self.balance = balance
        self.name=name


    def make_withdrawal(self,amount): #this is the method 1
        
        self.balance = self.balance-amount
    
    def make_deposit(self,amount):
        self.balance=self.balance+amount
    


    
    def display_user_balance(self): 
        
       
        print("balance" , self.balance,"name",self.name)


    def 


if __name__ == "__main__":
    user1 = User(500,"alaa")
    user2 = User(10000,"mohmmad")
    user3 = User(3000,"sami")

user1.make_deposit(1000)
##user1.make_deposit(300)
#user1.make_deposit(400)
user1.make_withdrawal(300)

user2.make_deposit(5000)
user2.make_deposit(5000)
user2.make_withdrawal(100)
user2.make_withdrawal(300)


user1.display_user_balance()