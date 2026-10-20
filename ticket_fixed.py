# GW, Vibe Code for a Theater

while True:
    try:
        age = int(input("Enter your age"))
        if age >= 0:
            break
        elif age < 0:
            print("Invalid Input")
    except:
        print("Invalid Input")
matinee = input("Is this a matinee? (yes/no): ").lower()

if age < 5:
    price = 0
elif age < 12:
    price = 8
elif age < 65:
    price = 12
else:
    price = 9

if matinee == "yes":
    price = price - 3

print(f"Ticket price: ${price}")
