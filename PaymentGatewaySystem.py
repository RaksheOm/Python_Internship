# step 1 
# Create Bank Account Class
# balance,pin

class BankAccount:
    def __init__(self,pin,balance=0):
        self.balance=balance
        self.pin=pin

        # method  to verify pin
    def verifyPin(self,user_pin):
        if user_pin != self.pin:
            raise ValueError("Invalid Pin...")
            
    def reset_pin(self,old_pin,new_pin):
        self.verifyPin(old_pin)
        self.pin=new_pin
        print("Pin reset....Done")

# b1=BankAccount("1234",20000)

class ATM:
    def __init__(self,account):
        self.account=account

    def withdraw(self,amount):
        if amount<=0:
            raise ValueError("Invalid Withdraw Amount..")
        if amount>self.account.balance:
            raise ValueError("Insufficient Balance...")
        self.account.balance-=amount
        print("Money Withdraw Successfully..")
        print("Your Current Balance is",self.account.balance)
    def deposit(self,amount):
        if amount<=0:
            raise ValueError("Invalid Deposit Amount...")
        self.account.balance+=amount
        print("Deposit Amount Successfully...")
        print("Your Current Balance Is ", self.account.balance)


    def checkbalance(self):   
        print("Your Current Balance Is ", self.account.balance)

# **************************************

# Main Interface
# These two lines initialize a bank account with a PIN ("12345") 
# and a starting balance of 1,000,000. Then, an ATM object (atm) is created,
#  which is tied to the account object. The ATM will interact with this account for the transactions.
# step 2 - User Interface
account=BankAccount("12345",1000000)
 # The ATM class is initialized with an account object
# (which could be any instance of BankAccount), and that account is stored in self.account.
atm=ATM(account)

try:
    your_pin=input("Enter Your Pin..")
    account.verifyPin(your_pin)

    print("\n ATM MENU...")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check balance")
    print("4. Reset Pin")
    print("5. Exit")

    choice=input("Choose Options..")
    match choice:
        case "1":
            amount=int(input("Enter Withdraw Amount"))
            atm.withdraw(amount)
        case "2":
            amount=int(input("Enter Deposit Amount"))
            atm.deposit(amount)
        case "3":
            atm.checkbalance()

        case "4":
            old__pin=input("Enter Your current pin :")
            new_pin=input("Enter Your New Pin :")
            account.reset_pin(old__pin,new_pin)
        case "5":
            print("Thanks Bro...")
        case _:
            print("Invalid Option....")
except Exception as e:
    print("Error Occured : ",e)


    
