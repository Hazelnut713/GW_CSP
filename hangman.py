# GW, Hangman Assignment
import random

# Create 1 file for a list of 10 words
words = []
with open("hangman.txt", "r") as file:
    content = file.read()
    words = content.split(",")
print(words)
# create another file that will just hold the win/loss count
win_lose = []
with open("win_loss.txt", "r") as file:
    content = file.read()
    win_lose = file.write(content)
print(win_lose)
# Use split(",") on the content of the words txt document to create your list of words

# Pull win and lose totals from the other txt file and save them as 2 seperate variables

# Build hangman game

# save the correct word as a varaiable random.choice(name of list)
# keep track of number of wrong guesses
# keep track of what letters have been guessed


# Function display the hangman (Needs number of wrong guesses)
#"""__________
#  |    |
#  |    O
#  |   /|\\
#  |   / \\
#  |_________
#"""

# Function to show the letters and spaces (The correct word, letters that have been guessesd)

# loop over the correct word
# variable for display word (starts as an empty string)
    # check if letter has been guessed
        # add the letter to the display word
    # if they haven't guessed the letter
        # add a underscore to the display word
# return the finished display (outside of the loop)

# Main game loop (while True)
# call function to show hangman
# print function call to show display word
# create variable for guessd letter
# add letter to guessed letters
# check to see if its not in the word
    # increase incorrect guesses
# check if display word is the same as the word
    # tell user they won
    # increase win count
    # ask if user wants to play again
        # reset random word, wrong guess count
# check to see if the lost (if they have 6 wrong guesses)
    # tell them they lost
    # tell them the word
    # increase lost count
    # ask if user wants to play again
        # reset random word, wrong guess count