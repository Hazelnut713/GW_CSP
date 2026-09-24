# GW, Password Strength Checker

password = input("Please make a password: ")
length = False
uppercase = False
lowercase = False
number = False
symbol = False
count = 0

if len(password) >= 8:
    length = True
    print(f"At least 8 characters: {length}")
else:
    print(f"At least 8 characters: {length}")

for letter in password:
    if letter.isupper():
        uppercase = True
    if letter.islower():
        lowercase = True
    if letter.isnumeric():
        number = True
    if letter in "!@#$%^&*()<>,./?|":
        symbol = True

if length == True:
    count = count + 1
if uppercase == True:
    count = count + 1
if lowercase == True:
    count = count + 1
if number == True:
    count = count + 1
if symbol == True:
    count = count + 1


print(f"Has uppercase letter: {uppercase}")
print(f"Has a lowercase letter: {lowercase}")
print(f"Has a number: {number}")
print(f"Has a symbol: {symbol}")
print(f"You have done {count}/5")
print("If you don\'t have 5/5 you should check if you have a uppercase letter, lowercase letter, a number, and a symbol.")