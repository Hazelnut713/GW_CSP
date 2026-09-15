# GW Hello User

while True:
    first_name = input("What is your first name: ").title().strip()
    last_name = input("What is your last name").title().strip()
    if first_name.isnumeric() + last_name.isnumeric():
        print("Sorry that is not a name")
    elif " " in first_name:
        break
    else:
        print("I said your first and last name")

print(f"hello {name}!")