import random

# ==========================================
#             HANGMAN GAME
# ==========================================

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    ========
    """
]

# Word categories
CATEGORIES = {
    "Animals": [
        "tiger", "elephant", "giraffe", "dolphin",
        "penguin", "kangaroo", "cheetah", "rabbit"
    ],
    "Sports": [
        "basketball", "soccer", "baseball", "tennis",
        "volleyball", "football", "hockey", "golf"
    ],
    "Movies": [
        "titanic", "avatar", "frozen", "jaws",
        "gladiator", "inception", "interstellar"
    ],
    "Technology": [
        "python", "computer", "keyboard", "internet",
        "software", "processor", "database", "algorithm"
    ],
    "Food": [
        "hamburger", "pizza", "sandwich", "pancakes",
        "chocolate", "spaghetti", "popcorn", "lasagna"
    ]
}

# Difficulty settings
DIFFICULTIES = {
    "1": {"name": "Easy", "lives": 8, "points": 10},
    "2": {"name": "Medium", "lives": 6, "points": 20},
    "3": {"name": "Hard", "lives": 4, "points": 30}
}


def print_title():
    print("\n" + "=" * 40)
    print("          H A N G M A N")
    print("=" * 40)
    print("       Guess the secret word!")
    print("=" * 40)


def choose_difficulty():
    print("\nChoose your difficulty:")
    print("1. Easy   - 8 lives, 10 points")
    print("2. Medium - 6 lives, 20 points")
    print("3. Hard   - 4 lives, 30 points")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]

        print("Invalid choice. Please enter 1, 2, or 3.")


def choose_category():
    category_names = list(CATEGORIES.keys())

    print("\nChoose a category:")
    for number, category in enumerate(category_names, start=1):
        print(f"{number}. {category}")
    print(f"{len(category_names) + 1}. Random category")

    while True:
        choice = input("Enter your choice: ").strip()

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(category_names):
                return category_names[number - 1]

            if number == len(category_names) + 1:
                return random.choice(category_names)

        print("Invalid choice. Try again.")


def display_word(word, guessed_letters):
    return " ".join(
        letter.upper() if letter in guessed_letters else "_"
        for letter in word
    )


def play_round(difficulty, category):
    word = random.choice(CATEGORIES[category]).lower()
    guessed_letters = set()
    wrong_letters = set()
    lives = difficulty["lives"]
    score = 0

    print(f"\nCategory: {category}")
    print(f"Difficulty: {difficulty['name']}")
    print(f"The word has {len(word)} letters.")

    while lives > 0:
        print("\n" + HANGMAN_PICS[
            min(
                len(HANGMAN_PICS) - 1,
                round(
                    (difficulty["lives"] - lives)
                    / difficulty["lives"] * 6
                )
            )
        ])

        print("Word:       ", display_word(word, guessed_letters))
        print("Wrong:      ", ", ".join(sorted(wrong_letters)) or "None")
        print(f"Lives left: {lives}")
        print(f"Round score: {score}")

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word!")
            score += lives * difficulty["points"]
            print(f"You earned {lives * difficulty['points']} bonus points!")
            return True, score

        guess = input("\nGuess a letter (or type 'hint'): ").lower().strip()

        if guess == "hint":
            remaining = [
                letter for letter in set(word)
                if letter not in guessed_letters
            ]

            if remaining:
                hint_letter = random.choice(remaining)
                guessed_letters.add(hint_letter)
                lives -= 1
                print(
                    f"Hint: The letter '{hint_letter.upper()}' "
                    "has been revealed. You lose one life!"
                )
            else:
                print("There are no letters left to reveal.")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter, or type 'hint'.")
            continue

        if guess in guessed_letters or guess in wrong_letters:
            print("You already guessed that letter!")
            continue

        if guess in word:
            guessed_letters.add(guess)
            gained = difficulty["points"] * word.count(guess)
            score += gained
            print(f"Correct! +{gained} points!")
        else:
            wrong_letters.add(guess)
            lives -= 1
            print("Wrong guess! You lost one life.")

    print(HANGMAN_PICS[-1])
    print(f"\nGame over! The word was: {word.upper()}")
    return False, 0


def main():
    total_score = 0
    games_played = 0
    wins = 0

    print_title()
    player_name = input("\nEnter your name: ").strip()

    if not player_name:
        player_name = "Player"

    print(f"\nWelcome, {player_name}!")

    while True:
        difficulty = choose_difficulty()
        category = choose_category()

        won, round_score = play_round(difficulty, category)

        games_played += 1
        total_score += round_score

        if won:
            wins += 1

        print("\n" + "=" * 40)
        print("             GAME RESULTS")
        print("=" * 40)
        print(f"Player:      {player_name}")
        print(f"Games played: {games_played}")
        print(f"Wins:         {wins}")
        print(f"Win rate:     {wins / games_played * 100:.1f}%")
        print(f"Total score:  {total_score}")
        print("=" * 40)

        while True:
            replay = input(
                "\nWould you like to play again? (y/n): "
            ).lower().strip()

            if replay in ("y", "yes"):
                break

            if replay in ("n", "no"):
                print(f"\nThanks for playing, {player_name}!")
                print(f"Final score: {total_score}")
                print("See you next time!")
                return

            print("Please enter y or n.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nThanks for playing Hangman. Goodbye!")
