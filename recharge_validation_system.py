# Create a function that allows a user to recharge their mobile number.

# **Requirements:**

# - Take **mobile number** and **recharge amount** as input
# - Mobile number must be **10 digits**
# - Recharge amount must be **greater than ₹10**
# - Handle invalid inputs using exception handling
# - Print success or failure message

# **Concepts to use:**

# - Function
# - `try-except`
# - `ValueError`


def recharge_mobile():
    try:
        mobile_number=input("Enter a Mobile Number : ")

        if len(mobile_number)!=10 or not mobile_number.isdigit():
            raise ValueError("Invalid Mobile Number ")

        recharge_amount=int(input("Give a recharge Amount : "))
        if recharge_amount<=10 :
            raise ValueError("Recharge Amount Must Be grater than 10")

        print("Recharge Successful")
        print("Mobile Number",mobile_number)
        print("Recharge Amount",recharge_amount)
    except Exception as err:
        print("Recharge Failed",err)

recharge_mobile()