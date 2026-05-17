# TASK 1: Simple Hangman Game

import random

# Predefined list of 5 words
words = ["apple", "tiger", "house", "plant", "chair"]

# Randomly choose one word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum wrong guesses allowed
wrong_guesses = 6

# Reward points
points = 0

print("Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")
print("Earn 10 points for every correct guess!\n")

while wrong_guesses > 0:
    display_word = ""

    # Show guessed letters and blanks
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Your Points:", points)

    # Check if word is fully guessed
    if "_" not in display_word:
        points += 50   # Bonus points
        print("\nCongratulations! You guessed the word:", word)
        print("Bonus +50 points!")
        print("Final Score:", points)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.\n")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Correct or wrong guess
    if guess in word:
        points += 10   # Reward points
        print("Correct guess! +10 points\n")
    else:
        wrong_guesses -= 1
        print("Wrong guess!")
        print("Remaining incorrect guesses:", wrong_guesses, "\n")

# If player loses
if wrong_guesses == 0:
    print("Game Over! The correct word was:", word)
    print("Your Final Score:", points)