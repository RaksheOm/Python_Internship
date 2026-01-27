# ### ** Electricity Bill Calculator**

# **Problem Statement:**

# Create a function to calculate electricity bill.

# **Rules:**

# - Units must be a positive number
# - Rate:
#     - 1–100 units → ₹5 per unit
#     - 101–300 units → ₹7 per unit
#     - Above 300 → ₹10 per unit
# - Handle invalid unit input (string, negative, empty)

# **Concepts to use:**

# - Function
# - `try-except`
# - `if-elif-else`
  
def calculateElectricityBill():
    try:
        number_of_units=int(input("Enter Number of Units : "))
        if number_of_units<=0:
            print("Unit must be greater than 0")
        elif number_of_units>=1 and number_of_units<=100:
            total_bill=number_of_units*5
        elif number_of_units>=101 and number_of_units<=300:
            total_bill=number_of_units*7
        elif number_of_units>300:
            total_bill=number_of_units*10
        print("Total Electricity Bill :",total_bill)

        
    except ValueError:
        print("Please Enter Numeric value as input")

calculateElectricityBill()