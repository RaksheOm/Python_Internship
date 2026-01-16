
# Tuple: Tuple is collection of similar  or different type of element
# syntax -()
# immutable


# skill=("HTML","CSS","JS")

# # 2- second method withot ( )
# emp="HTML","CSS","JS"
# print(type(emp))

emp=("HTML",)
print(type(emp))
sorted(emp)
print(emp)


# 4️⃣ Count how many times `"apple"` appears in `("apple", "banana", "apple")`.

# 5️⃣ Unpack a tuple `(10, 20, 30)` into 3 variables.

# 6️⃣ Create a nested tuple and access the second row, third element.
# 1️⃣ Create a tuple of 5 colors and print them one by one.


# 4️⃣ Count how many times `"apple"` appears in `("apple", "banana", "apple")`.
tuple_1=("apple", "banana", "apple")
print(tuple_1.count("apple"))


# 5️⃣ Unpack a tuple `(10, 20, 30)` into 3 variables.
tuple_2=(10, 20, 30)
m1,m2,m3=tuple_2
print(tuple_2)

# 6️⃣ Create a nested tuple and access the second row, third element.
tuple_3=(
    
    ("Om", "Aditya","Onkar","Sanmesh"),
    ("Om", 20,49,45)
)
print(tuple_3[1][2])

# 1️⃣ Create a tuple of 5 colors and print them one by one.
tuple_4=("Red","Green","Pink","Orange","White")
for x in tuple_4:
    print(x)