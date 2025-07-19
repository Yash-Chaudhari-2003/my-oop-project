class Atm:
    
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()
        
    def menu(self):
        
        User_input = input("""
              1. Press 1 to set a pin
              2. Press 2 to change pin
              3. Press 3 to check balance
              4. Press 4 to withdraw
              5. anything else exit """)
        
        if User_input == '1':
            #Set a pin
            self.create_pin()
            
        elif User_input == '2':
            #Change a pin
            self.Change_pin()
            
        elif User_input == '3':
            #Check balance
            self.check_balance()
            
        elif User_input == '4':
            #Withdraw
            self.Withdraw()
        else:
            exit
            
    def create_pin(self):
        user_pin = input("Enter the pin: ")
        self.pin = user_pin
        
        user_balance = int(input("Enter your balance: "))
        self.balance = user_balance
        self.menu()
        
    def Change_pin(self):
        old_pin = input("Enter your old pin: ")
        
        if old_pin == self.pin:
            new_pin = input("Enter your new pin: ")
            self.pin = new_pin
        self.menu()
        
    def check_balance(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            print("your bank balance is: ", self.balance)
        else:
            print("sorry pin is incorrect")
        self.menu()
        
    def Withdraw(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            amount = int(input("Enter amount you want to withdraw: "))
            if amount<=self.balance:
                self.balance = self.balance - amount
                print("withdraw successful, the remining ammount is ", self.balance)
            else:
                print("Your account has not that much of amount")
        else:
            print("The pin is wrong. Try again")
        self.menu()
        
    
MyAtm = Atm()

        