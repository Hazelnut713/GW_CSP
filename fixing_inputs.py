# GW, Fixing Inputs

# When you want a specific input
while True:
    color = input("Tell me a color that is only 1 word: ").lower().strip()
    if color.isnumeric():
        print("sorry that is a number")
    elif " " in color:
        print("I said one word")
    else:
        break

print(f"I painted you walls {color}!")

# when you want a number
while True:
    try:
        age = int(input("How old are you: "))
        break
    except:
        print("That isn't a number")

print(f"Wow you are {age} that is really old!")