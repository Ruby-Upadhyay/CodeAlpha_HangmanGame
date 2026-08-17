import random

# Display the game title and instructions
print("===============================")
print("        HANGMAN GAME")
print("===============================")
print("Guess the hidden word!")
print("You have 6 wrong guesses.")

# List of words from which the secret word will be selected
words = ["Press","Delhi","India","kurta","Maths"]

# Select a random word
word = random.choice(words)

# Create underscores to hide the letters of the word
hidden_word = ["_"] * len(word)
print(" ".join(hidden_word))

# Track the number of wrong guesses and previously guessed letters
wrong_guesses = 0
guessed_letters = []

# Continue the game until the player makes 6 wrong guesses
while wrong_guesses < 6:

    # Take a letter as input from the player
    guess = input("Guess a letter: ").lower()

    # Validate the player's input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You already guessed this letter.")
    else:
        guessed_letters.append(guess)

        # Check if the guessed letter is present in the secret word
        if guess in word.lower():
            print("Correct guess!")

            # Reveal all positions where the guessed letter appears
            for i in range(len(word)):
                if word[i].lower() == guess:
                    hidden_word[i] = guess
        else:
            print("Incorrect guess!")
            wrong_guesses += 1

        # Display the current progress of the word
        print(" ".join(hidden_word))
        print("Wrong guesses:", wrong_guesses)

        # Check if all letters have been guessed
        if '_' not in hidden_word:
            print("Congratulations! You won the game!")
            break

# Display the game over message if all attempts are used
if wrong_guesses == 6:
    print("Game Over!")
    print("The word was:", word)
