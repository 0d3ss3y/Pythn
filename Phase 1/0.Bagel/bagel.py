import platform
import random
import os

def main():
    heading()
    rules()
    number = generate_random_number()
    play_game(number)
    continueGame()

def continueGame():
    ans = input("Would you like to play again? (y/n) ")[0].upper()
    if ans == 'Y':
        clear_screen()
        main()
    else:
        print("Thank you for playing!")


def clear_screen():
    # Check the operating system
    if platform.system() == "Windows":
        os.system('cls')  # For Windows
    else:
        os.system('clear')

def play_game(number):
    guesses = 0
    position = 0
    digits = 0
    while guesses < 10:
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

    else:
        print("Sorry, you lost!")

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