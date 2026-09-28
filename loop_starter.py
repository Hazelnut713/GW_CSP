# GW, Loop counts to 20 by 2

# Nessting is when you put one block of code into another block of code

"""for number in range(0,21,2):
    print(number)"""
csp = ["Remy", "Alex", "Gabe", "Bliss"]
if len(csp) > 0:
    for student in csp:
        print(f"Checking in {student}")
else:
    print("There is no one in class")


while True:
    username = input("What is your username: ").strip()
    password = input("What is your password: ").strip()

    if username == "LaRose4" and password == "password":
        print("Welcome to the program! ")
        break
    else:
        print("Those credentials were incorrect.")