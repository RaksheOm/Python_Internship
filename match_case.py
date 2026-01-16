# match case

# used to handle multiple cases at a same time
# handle multiple operations at a same time

# syntax

# match choice:
#     case 1:
#     case 2:
#     case 3:
#     case _:default case



day=int(input("Enter A Day..."))
print(type(day))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")

    # default case
    case _:
        print("Invalid Day No....")


# **********************************



number1=int(input("ENter No 1 : "))
number2=int(input("Enter Number 2: "))

operator=input("Choose Any One of These : + ,  - , / ,  * , %   =.  ")

match operator:
    case "+":
        print("Addition Is ", number1+number2)
    case "-":
        print(f" Subtraction Is {number1} - {number2} = {number1-number2}")
    case "*":
        print(f"Multiplication Is {number1}*{number2} = {number1*number2}")
    case "/":
        print(f"Division Is {number1}/{number2} = {number1/number2} ")
    case "%":
        print(f"Modulus Is {number1}%{number2} = {number1%number2} ")
    case "//":
        print(f"Modulus Is {number1}//{number2} = {number1//number2} ")
    case _:
        print("Choose valid Operation.....")


 # ********************************************


day=input("Enter A Day")


# wrong code

# match day:
#     case "monday":
#     case "tuesday":
#     case "wednesday":
#     case "thursday":
#     case "friday":
#         print("It's A Weekday...")
#     case "saturday":
#     case "sunday":
#         print("Weekend")
#     case _:
#         print("Invalid day....")




# # 2
# day = input("Enter the day: ")

# match day:
#     case "saturday" | "sunday":
#         print("It's a Weekend")
#     case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
#         print("It's a weekday")
#     case _:
#         print("Invalid ")
        

# # 3
# day = input("Enter a day: ").lower()

if day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    print(day, "is a Weekday")
elif day in ["saturday", "sunday"]:
    print(day, "is a Weekend")
else:
    print("Invalid day! Please enter a valid weekday name.")



