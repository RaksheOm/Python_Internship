# Q: Reverse a string without using reverse function
# 👉 What to observe: loop logic, indexing

# 2️⃣ Number Logic

# Q: Check whether a number is palindrome
# Example: 121 → Yes, 123 → No

# 3️⃣ Counting Logic

# Q: Count vowels in a string
# Extra follow-up: Ignore case?

# 4️⃣ List Logic

# Q: Find duplicate elements in a list
# Follow-up: Without using set()



# Task-1:

# A=input()
# reverse_string=""
# for i in A:
#     reverse_string=str(i)+reverse_string
# print(reverse_string)

# Task-2:
# A=input()
# reverse_string=""
# for i in A:
#     reverse_string=str(i)+reverse_string
# if A==reverse_string:
#     print("Number is Pallindrome")
# else:
#     print("Not a pallindome")

# Task-3
# string=input()
# vowels="aeiou"
# count=0
# for i in string:
#     if i in vowels: #in vowels means aeiou
#         count+=1
# print(count)

# Task-4
# 4️⃣ List Logic
# Q: Find duplicate elements in a list
# Follow-up: Without using set()


# list1=[1,3,1,2]
# duplicate=""
# for i in list1:
#     if list1.count(i) > 1 and str(i) not in duplicate:
#         duplicate=duplicate+str(i)
# print(duplicate)



