
# class A:
#     acc_no=2132615

#     emp_CTC="20LPA"
#     def acc_holder(self,user_name,user_id):
#         self.user_name=user_name
#         self.user_id=user_id

# user1=A()
# result=user1.acc_holder("Om",123)
# print(result)

# # name mangling - To accesss private variable
# print(result._A__empCTC)

# class Account:
#     try:
#         def __init__(self):
#             self.__balance = 0

#         def deposit(self, amount):
#             self.__balance += amount

#         def withdraw(self, amount):
#             if amount <= self.__balance:
#                 self.__balance -= amount
#             else:
#               print("Insufficient Balance")

#         def check_balance(self):
#          return self._balance
        
#     except Exception as e:
#         print("Error: ",e)

# acc = Account()
# acc.deposit(500)
# print(acc.check_balance())
# acc.withdraw(200)
# print(acc.check_balance())


# class Account:
#     def __init__(self):
#         self.__balance = 0

#     def deposit(self, amount):
#         try:
#             if amount <= 0:
#                 raise ValueError("Deposit amount must be positive")
#             self.__balance += amount
#         except Exception as e:
#             print("Deposit Error:", e)

#     def withdraw(self, amount):
#         try:
#             if amount <= 0:
#                 raise ValueError("Withdrawal amount must be positive")
#             if amount > self.__balance:
#                 raise ValueError("Insufficient Balance")
#             self.__balance -= amount
#         except Exception as e:
#             print("Withdraw Error:", e)

#     def check_balance(self):
#         return self.__balance

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return ( self.__balance)
acc = BankAccount(1000)

acc.deposit(500)
acc.withdraw(300)

print(acc._BankAccount__balance())  
