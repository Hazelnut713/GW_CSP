# GW, Number Guessing Game
import random

attemps = 1

for number in range(1,3):
    guess = input(f"Guess #{attemps}: ")
    if guess < number:
        attemps += 1
        print("That is too low")
        continue
    elif guess > number:
        attemps += 1
        print("That is too high")
        continue
    else:
        print(f"Wow you got it right in {attemps} good job")
        break