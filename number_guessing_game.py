# GW, Number Guessing Game
import random

attemps = 1



while attemps <= 6:
    while True:
        guess = input(f"Guess #{attemps}: ")
        guess = int(guess)
        for number in range(1,3):
            if guess == number:
                print(f"You got it in {attemps} good job!")
                break
            elif guess < number:
                print("That was too low try again: ")
                attemps += 1
            else:
                print("That was too high try again")
                attemps += 1