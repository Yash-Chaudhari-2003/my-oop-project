class Account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    
    def deposite(self,amount):
        if amount<=0:
            print("Deposite amount must be postive")
            return
        self.balance += amount
        print(f"{amount} deposite successfully. New balance: {self.balance}")
        
    def withdraw(self, amount):
        if amount<=0:
            print("withdraw amount must be positive")
        elif amount>self.balance:
            print("insufficient funds")
        else:                                          
            self.balance -= amount
            print(f"{amount} is withdraw successfully. Remaning balance: {self.balance}")
            
    def check_balance(self):
        print(f"{self.name}, your balance is {self.balance}")