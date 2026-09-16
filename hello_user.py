# GW Hello User

while True:
    name = input("What is your name: ").title().strip()
    if name.isnumeric():
        print("Sorry that is not a name")
    else:
        break

print(f"hello {name}, nice to meet you")