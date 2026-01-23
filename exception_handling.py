# try:
#     def Calci(a,b):
#         return a/b
    
#     res=Calci(50,0)
#     print(res)
# except Exception as err:
#     print("error occured :",err)

# try:
#     x=100
#     b=300
#     print(a+b)
# except ValueError:
#     prit("Invalid data type")
# except NameError:
#     print("Name error")
# finally:
#     print("Code executed successfully")
    
# try:
#     a=20
#     b="pratik"
#     print(a+b)
# except:
#     print("Error Occured")


# try:
#     def Calci(a,b):
#         return a/b
#     print(Calci(5,5))
#     res=Calci(50,0)
#     print(res)
    
# except Exception as err:
#     print("Error Occured",err)

# print("Hello")

# try:
#     age=int(input("enter your age: "))
#     def demo(a):
#         if(age<=0 or age<=100):
#             raise ValueError("age can not be negative or greater then 100") # raise handle self error
#         print("your age is",age)
        
#     demo(age)
# except Exception as e:
#     print("error",e)
    
    
# Task - Take Username Inout From User
# Rules:

# cannot be empty
# length must be at least 4
# must not contain  spaces

# if fails- raise ValueErro

try:
    UserName=input("Enter UserName: ")
    def demo(u):
        if u==" ":
            raise ValueError("UserName cannot be empty")
        if len(u)<4:
            raise ValueError("length must be atleast 4")
        if " " in u:
            raise ValueError("Username must not contain spaces")

        print("Username is valid:", u)
    
    
    demo(UserName)
    
except Exception as e:
    print("Error:", e)
    
    

