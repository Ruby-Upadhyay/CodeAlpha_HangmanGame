# CodeAlpha Internship – Task 1: Hangman Game

A simple text-based Hangman Game developed using Python as part of the **CodeAlpha Python Programming Internship**.

## Project Overview

This project is a console-based Hangman Game in which the player tries to guess a randomly selected hidden word one letter at a time.

The player has a maximum of 6 incorrect guesses. The game keeps track of correct and incorrect guesses and displays the player's progress until the word is completely revealed or all attempts are used.

## Features

- Random word selection
- Hidden word display
- Letter-by-letter guessing
- Correct and incorrect guess handling
- Input validation
- Repeated guess detection
- Maximum 6 wrong guesses
- Correctly guessed letter display
- Wrong guess tracking
- Win condition
- Game Over condition

## Technologies Used

- Python
- `random` Module
- Lists
- Loops
- Conditional Statements
- String Manipulation
- User Input

## How the Game Works

1. The program randomly selects a word from a predefined list.
2. The selected word is hidden using underscores.
3. The player guesses one letter at a time.
4. If the guessed letter is present in the word, it is revealed.
5. If the guessed letter is incorrect, the wrong-guess count increases.
6. The player can make a maximum of 6 incorrect guesses.
7. Previously guessed letters are detected to prevent repeated guesses.
8. The player wins when all letters of the word are revealed.
9. The game ends when the player reaches 6 incorrect guesses.

## Input Validation

The program validates the player's input before processing the guess.

It checks that:

- The input contains only a single alphabetic character.
- The same letter is not guessed repeatedly.
- Invalid input is rejected and the player is asked to enter a valid letter.

## Project Files

- `Hangman.py` — Main Python program
- `README.md` — Project documentation

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Open the Project

Open the project folder in VS Code.

### 3. Open the Terminal

Open the VS Code terminal and navigate to the project folder.

### 4. Run the Game

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

## Internship Task

This project was developed as **Task 1: Hangman Game** for the **CodeAlpha Python Programming Internship**.

The task focuses on implementing a simple text-based game using Python programming fundamentals, random word selection, user input, loops, conditional statements, and basic game logic.
