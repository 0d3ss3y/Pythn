
# Bagels - A Deductive Logic Game

**Bagels** is a fun, simple, and engaging deductive logic game where players attempt to guess a secret three-digit number based on clues provided after each guess. 

## How to Play

The objective of **Bagels** is to guess the secret three-digit number within **10 tries**. After each guess, you will receive a hint that helps you determine how close your guess is to the secret number.

### Hints

The game provides one of three types of hints:

- **Pico**: One of the digits in your guess is correct but in the wrong position.
- **Fermi**: One of the digits in your guess is both correct and in the correct position.
- **Bagels**: None of the digits in your guess are correct.

Using these clues, refine your guesses to deduce the secret number within the allowed attempts.

## Example Gameplay

1. Suppose the secret number is **427**.
2. You guess **123**.
   - **Hint:** "Pico" (1 and 2 are incorrect, but 3 is a correct digit in the wrong position)
3. You guess **247**.
   - **Hint:** "Fermi" (4 and 2 are correct and in the correct position)

Continue making educated guesses using the hints until you guess the correct number or exhaust your 10 tries.

## Requirements

- Python 3.x or later (if implementing in Python).
- No additional dependencies.

## Installation

1. Clone or download the project files.
2. Run `bagels.py` (or your implementation) to start the game.

Enjoy cracking the code with Bagels!
