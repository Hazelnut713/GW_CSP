import random

print("I have a number try to guess it")
number = random.randint(1,101)
attemps = 1

while attemps <= 6:
    while True:
        try:
            guess = int(input(f"Guess #(attemps): "))
            break
        except:
            print("That wasn't a number")

    if guess > number:
        print("That's too high")
    elif guess < number:
        print("That's too low")
    else:
        break
    attemps += 1
if attemps <= 6:
    print(f"Good job you guessed my number in {attemps} tries.")
else:
    print(f"You are out of guesses. The number was {number}. Better luck next time.")