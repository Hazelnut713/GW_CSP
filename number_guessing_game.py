# GW, Number Guessing Game
import random

attemps = 1

for number in range(1,3):
    guess = input(f"Guess #{attemps}: ")
    if guess == number:
        print(f"Wow you guessed it in {attemps} try")
    elif guess != number:
        if guess < number:
         print("That was to low")
        elif guess > number:
           print("That was to high")
        guess = input("Guess a second number: ")
    elif guess != number:
        print()


