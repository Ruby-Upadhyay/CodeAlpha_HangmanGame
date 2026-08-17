# Hangman Game

A simple text-based Hangman game developed using Python as part of the CodeAlpha internship.

## Features

- Random word selection
- Hidden word display
- Letter-by-letter guessing
- Input validation
- Repeated guess detection
- Maximum 6 wrong guesses
- Correct letter revealing
- Win and Game Over conditions

## Technologies Used

- Python
- Random module

## How the Game Works

1. The program randomly selects a word from a list.
2. The letters of the word are hidden using underscores.
3. The player guesses one letter at a time.
4. If the guessed letter is correct, it is revealed.
5. Incorrect guesses increase the wrong-guess count.
6. The player can make up to 6 wrong guesses.
7. The player wins when all letters are revealed.
8. The game ends if 6 wrong guesses are made.

## Input Validation

The game checks the player's input and accepts only a single alphabetic character.

It also prevents the same letter from being guessed repeatedly.

## How to Run

Make sure Python is installed on your computer.

Run the following command in the terminal:

```bash
python Hangman.py
```

## Example

```text
===============================
        HANGMAN GAME
===============================
Guess the hidden word!
You have 6 wrong guesses.
_ _ _ _ _

Guess a letter: e
Correct guess!
_ e _ _ _
Wrong guesses: 0
```

## Project

This project was created as part of the CodeAlpha Python Programming Internship.
