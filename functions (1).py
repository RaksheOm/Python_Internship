
print("hello welcome to function")

# function- is a block of code i.e is a bunch of statements / mini program inside your program
# we can reused functions multiple times by calling
# defined once and reused multiple times
# syntax:

'''

syntax

# function defination/declartion
def function_name():
    #block of code will execute

# function_call
function_name()

eg

def demo():
    print("hello world)

demo()

'''


def greet():
    print("Welcome To Our Program")

greet()


# ********************

def addition():
    print(20+40)

addition()
addition()

# ***********************************************

# to pass dynamic values inside function

# parameters - value which we passed during function declartion/defination
# arguments-Actual values which we pass while function calling 

def Sum(a,b):
    print(a+b)

Sum(30,40) # 70
Sum(100,200)

# ***********************


def checkEligibility(age):
    if(age>=18):
        print("COngrats....")
    else:
        print("Sorry")
    
userAge=int(input("Enter Your Age....."))
checkEligibility(userAge)
# checkEligibility(10)11


def UserInfo(userName,userSkill,userAddress):
    print(f"Your Name is {userName}, Your Skill is {userSkill} and your Address is {userAddress}")

UserInfo("Nishant","Python","Pune")
UserInfo("ABC","React JS","Pune")

# *****************************************************

# Account_Balance=100000

def deposit(balance):
    amount = int(input("Enter deposit amount: "))
    
    if amount <= 0:
        print("Invalid deposit amount")
        return balance

    balance += amount
    print("Account Balance:", balance)
    return balance


def withdraw(balance):
    amount = int(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Invalid withdrawal amount")
        return balance

    if amount > balance:
        print("Insufficient balance")
        return balance

    balance -= amount
    print("Account Balance:", balance)
    return balance


def main():
    account_balance = 100000

    action = input("Would you like to deposit or withdraw? (deposit/withdraw/no): ").lower()

    match action:
        case "deposit":
            account_balance = deposit(account_balance)
        case "withdraw":
            account_balance = withdraw(account_balance)
        case "no":
            print("Account Balance:", account_balance)
        case _:
            print("Invalid choice")


main()

# ******************************************





        

