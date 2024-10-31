import random
from string import digits


def main():
    heading()
    rules()
    number = generate_random_number()
    play_game(number)


def play_game(number):
    guesses = 0
    position = 0
    digits = 0
    print(number)
    while guesses <= 3:
        guesses += 1
        print(f"Guess #{guesses}")
        guess = input("> ")

        if not guess.isdigit() or len(guess) != 3:
            print("Please enter a valid 3-digit number.")
            continue

        if guess == str(number):
            print("Congratulations! You guessed the number!")
            break

        else:

            for i in range(len(guess)):
                if guess[i] == str(number)[i]:
                    digits += 1
                elif guess[i] in str(number):
                    position += 1

            if position > 0:
                print("Pico "*position)

            elif digits > 0:
                print("Fermi "*digits)

            else:
                print("Bagels")

            position = 0
            digits = 0


def generate_random_number():
    return random.randint(100, 999)

def rules():
    print("""
I am thinking of a 3-digit number. Try to guess what it is.

Here are some clues:
When I say: That means:
 Pico One digit is correct but in the wrong position.
 Fermi One digit is correct and in the right position.
 Bagels No digit is correct.
    """)

def heading():
    print("Bagels, a deductive logic game.")


if __name__ == '__main__':
    main()