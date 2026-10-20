# GW, Vibe code for a Theater assignment

age = int(input("Enter your age: ")) # allows negatives and completely breaks with non whole numbers when it should say invalid number and ask again when it either breaks or continues syntax
matinee = input("Is this a matinee? (yes/no): ").lower()


if age < 5:
    price = 0
elif age < 12: # when you are 12 it should be 8 dollars but is 12 dollars syntax
    price = 8
elif age < 65:
    price = 12
else:
    price = 9

if matinee == "yes": # allows price below 0 when it shouldn't affect the price of the people 5 and under syntax
    price = price - 3

print(f"Ticket price: ${price}") # doesn't print the 2 decimal points when it should be followed by .00 it is followed by nothing syntax
