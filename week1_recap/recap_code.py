# # Python recap 27/8/26
# # Comments with # 

# # Print statements
# print("Hello, World!")

# name = "Aurélien"
# age = 26

# # Behaviour 1
# print(name + " is " + str(age) + " years old.")   # This will break # fixed 
# # Behaviour 2
# print(name, "is", age, "years old.")
# # Behaviour 3
# print(f"{name} is {age} years old.")

# # Input is always a string
# age2 = input("How old is the other person?")

# age3 = age + int(age2)   # This will break # fixed

# # Control flow: selection
# if age3 >= 18:
#     print("Allowed to have beer.")
# else:
#     print("Need to wait.")

# # match / case
# choice = input("Enter your selection")

# match choice:
#     case "1":
#         print("First option")
#     case "2":
#         print("Second option")
#     case _:
#         print("Anything else...")


# Loops - for

for index in range(5):
    print(index) 

correct_password = "markogg"
password = ""

while password != correct_password:
    password = input("What is the password?")
    

def print_reverse(some_string):
    print(some_string[::-1])

something = input("enter a string")
print_reverse(something)

