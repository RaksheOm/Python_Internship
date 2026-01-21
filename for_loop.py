         # mcq-1

# book="Alchemist"
# result=""
# length=len(book)

# for i in range(length):
#     result=result+book[length-i] #length=9 i=0 9-0==9 not exist so error is their
# print(result)  #index error

         # msq-2
# number=453
# result=""
# for i in str(number):
#     result=i + result # '4'+""=="4" result
#                     # '5'+"4"=="54"
#                     # '3'+"54"=="354"
# print(result)   #354      

        #mcq-3
# n1=int(input())
# n2=int(input())
# for i in range(n1,n2):
#     print(i)     #15 16 17 18

        #mcq-4
# n=input()   #1079
# sum_of_numbers=0

# for i in n:
#     sum_of_numbers=sum_of_numbers + int(i)  # 0+1==1
# print(sum_of_numbers)  #17

        #mcq-5
# count=0
# for i in range(1,8):
#     count=count*1
# print(count)   # 0 because count==0

        #mcq=6
# animal="Lion" #0123
# result=""
# for i in range(len(animal)):
#     result=result+(animal[i]*i)
# print(result)  #ioonnn

        # mcq-7
# word="Hello World"
# result=""
# for i in word:
#     if i != " ":
#         result=result+i
# print(result)

        # mcq-8
# book="Wings of Fire"
# for i in range(len(book)):
#     if book[i] == "e":
#         print(book[:i])  #Wings of Fir

        # mcq-9
# animal="Cat"
# total=""
# for i in range(len(animal)):
#     total=total+animal[i]
#     print(total) #C
                #Ca
                #Cat
                
        #mcq-10
# verb="Run"
# result=""
# for i in range(len(verb)):
#     if(i==len(verb)-1):
#         result=result+verb[i]
#     else:
#         result=result + verb[i] + " "   
# print(result) # R u n

        # mcq-11
for i in "Learn":
    print(i)